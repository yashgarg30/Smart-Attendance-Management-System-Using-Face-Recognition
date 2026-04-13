from tkcalendar import DateEntry
import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os

from register import register_user
from train import train_model
from attendance import start_attendance
from database import connect_db


def register_and_train():

    def submit():

        student_id = id_entry.get().strip()
        name = name_entry.get().strip()

        if student_id == "" or name == "":
            messagebox.showerror("Error", "All fields are required")
            return

        win.destroy()

        register_user(student_id, name)

        messagebox.showinfo("Info", "Training model... Please wait")
        train_model()
        messagebox.showinfo("Success", "User Registered and Model Trained!")

    win = tk.Toplevel()
    win.title("Register User")
    win.geometry("300x200")

    tk.Label(win, text="Student ID").pack(pady=5)
    id_entry = tk.Entry(win)
    id_entry.pack(pady=5)

    tk.Label(win, text="Student Name").pack(pady=5)
    name_entry = tk.Entry(win)
    name_entry.pack(pady=5)

    tk.Button(win,
              text="Start Registration",
              command=submit,
              bg="#27ae60",
              fg="white").pack(pady=10)


def start_attendance_gui():
    if not os.path.exists("trainer/trainer.yml"):
        messagebox.showerror("Error", "Model not trained!\nRegister user first.")
        return
    start_attendance()


def view_attendance_records():

    import datetime
    from tkcalendar import DateEntry
    from openpyxl import Workbook
    from tkinter import filedialog

    records_cache = []

    def fetch_records(selected_date):

        nonlocal records_cache
        records_cache = []

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, name, date, time FROM attendance WHERE date=%s ORDER BY time",
            (selected_date,)
        )

        records = cursor.fetchall()
        conn.close()

        for item in tree.get_children():
            tree.delete(item)

        count = 0
        for row in records:
            tree.insert("", "end", values=row)
            records_cache.append(row)
            count += 1

        total_label.config(text=f"Total Present: {count}")

        if count == 0:
            messagebox.showinfo("Info", "No attendance found for this date")

    def fetch_selected():
        selected_date = cal.get_date()
        fetch_records(selected_date)

    def fetch_today():
        today = datetime.date.today()
        cal.set_date(today)
        fetch_records(today)

    def download_report():

        if len(records_cache) == 0:
            messagebox.showerror("Error", "No data to export")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel File", "*.xlsx")],
            title="Save Report"
        )

        if not file_path:
            return

        wb = Workbook()
        ws = wb.active
        ws.title = "Attendance Report"

        ws.append(["Student ID", "Student Name", "Date", "Time"])

        for row in records_cache:
            ws.append(row)

        wb.save(file_path)

        messagebox.showinfo("Success", "Report Downloaded Successfully!")

    win = tk.Toplevel()
    win.title("Attendance Records")
    win.geometry("800x520")

    top_frame = tk.Frame(win)
    top_frame.pack(pady=10)

    tk.Label(top_frame, text="Select Date:", font=("Arial", 11)).pack(side="left", padx=5)

    cal = DateEntry(top_frame, width=12,
                    background='darkblue',
                    foreground='white',
                    borderwidth=2,
                    date_pattern='yyyy-mm-dd')
    cal.pack(side="left", padx=5)

    tk.Button(top_frame,
              text="Show Attendance",
              command=fetch_selected,
              bg="#2980b9",
              fg="white").pack(side="left", padx=5)

    tk.Button(top_frame,
              text="Show Today",
              command=fetch_today,
              bg="#27ae60",
              fg="white").pack(side="left", padx=5)

    tk.Button(top_frame,
              text="Download Report",
              command=download_report,
              bg="#8e44ad",
              fg="white").pack(side="left", padx=5)

    total_label = tk.Label(win,
                           text="Total Present: 0",
                           font=("Arial", 12, "bold"))
    total_label.pack(pady=5)

    table_frame = tk.Frame(win)
    table_frame.pack(fill="both", expand=True)

    scrollbar = tk.Scrollbar(table_frame)
    scrollbar.pack(side="right", fill="y")

    tree = ttk.Treeview(table_frame,
                        columns=("ID", "Name", "Date", "Time"),
                        show="headings",
                        yscrollcommand=scrollbar.set)

    scrollbar.config(command=tree.yview)

    tree.heading("ID", text="Student ID")
    tree.heading("Name", text="Student Name")
    tree.heading("Date", text="Date")
    tree.heading("Time", text="Time")

    tree.column("ID", width=120)
    tree.column("Name", width=200)
    tree.column("Date", width=150)
    tree.column("Time", width=150)

    tree.pack(fill="both", expand=True)

def exit_app():
    root.destroy()


root = tk.Tk()
root.title("Smart Attendance System")
root.geometry("420x380")
root.configure(bg="#2c3e50")


title = tk.Label(root,
                 text="SMART ATTENDANCE SYSTEM",
                 font=("Arial", 16, "bold"),
                 bg="#2c3e50",
                 fg="white")
title.pack(pady=20)


btn_register = tk.Button(root,
                         text="Register User",
                         font=("Arial", 12),
                         width=22,
                         height=2,
                         command=register_and_train,
                         bg="#27ae60",
                         fg="white")
btn_register.pack(pady=10)


btn_attendance = tk.Button(root,
                           text="Start Attendance",
                           font=("Arial", 12),
                           width=22,
                           height=2,
                           command=start_attendance_gui,
                           bg="#2980b9",
                           fg="white")
btn_attendance.pack(pady=10)


btn_records = tk.Button(root,
                        text="View Attendance Records",
                        font=("Arial", 12),
                        width=22,
                        height=2,
                        command=view_attendance_records,
                        bg="#8e44ad",
                        fg="white")
btn_records.pack(pady=10)


btn_exit = tk.Button(root,
                     text="Exit",
                     font=("Arial", 12),
                     width=22,
                     height=2,
                     command=exit_app,
                     bg="#c0392b",
                     fg="white")
btn_exit.pack(pady=10)


root.mainloop()