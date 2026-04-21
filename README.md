# 📸 Smart Attendance System using Face Recognition

## 📌 Overview

The **Smart Attendance System** is an automated solution that uses face recognition technology to mark attendance in real-time. It eliminates manual effort, prevents proxy attendance, and provides a secure, contactless, and efficient way of managing attendance records.

The system is built using **Python**, **OpenCV**, and **MySQL**, with a user-friendly GUI developed using **Tkinter**.

---

## 🎯 Features

- 👤 User Registration with face capture
- 🧠 Face Recognition using LBPH algorithm
- 🎥 Real-time attendance marking via webcam
- 🗄️ MySQL database integration
- 📅 Date-wise attendance filtering
- 📊 Total attendance count
- 📥 Download attendance report in Excel format
- 🖥️ GUI-based application (no terminal usage)

---

## 🛠️ Technologies Used

| Category | Details |
|---|---|
| Programming Language | Python |
| Libraries | OpenCV, NumPy, Pillow, Tkinter |
| Database | MySQL |
| Excel Handling | OpenPyXL |
| Algorithm | LBPH (Local Binary Pattern Histogram) |

---

## 📂 Project Structure

```
smart_attendance/
│
├── dataset/                  # Stored face images
├── trainer/                  # Trained model & labels
│   ├── trainer.yml
│   └── labels.json
│
├── register.py               # User registration
├── train.py                  # Model training
├── attendance.py             # Face recognition & attendance
├── database.py               # MySQL connection
├── main.py                   # GUI application
├── reset_system.py           # Reset system (optional)
├── schema.sql                # Database schema
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/smart-attendance-system.git
cd smart-attendance-system
```

### 2️⃣ Install Dependencies

```bash
pip install opencv-python
pip install opencv-contrib-python
pip install numpy
pip install pillow
pip install mysql-connector-python
pip install openpyxl
pip install tkcalendar
```

### 3️⃣ Setup MySQL Database

Run the following SQL:

```sql
CREATE DATABASE smart_attendance;

USE smart_attendance;

CREATE TABLE students (
    id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE attendance (
    id VARCHAR(20),
    name VARCHAR(100),
    date DATE,
    time TIME
);
```

### 4️⃣ Configure Database

Update your MySQL credentials in `database.py`:

```python
password="your_password"
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🧑‍💻 Usage

### 🔹 Register User
1. Enter Student ID and Name
2. System captures face images
3. Model is trained automatically

### 🔹 Start Attendance
1. Camera opens
2. Recognizes registered users
3. Marks attendance automatically

### 🔹 View Attendance Records
1. Select date using calendar
2. View attendance table
3. See total present count

### 🔹 Download Report
- Export attendance data to Excel file

---

## 🔄 Reset System *(Optional)*

To clear all data:

```bash
python reset_system.py
```

---

## 📊 Example Output

| Status | Output |
|---|---|
| ✅ Recognized User | `23BAI70023 - Yash` |
| ❌ Unknown User | `Unknown` |

---

## ⚠️ Limitations

- Performance depends on lighting conditions
- Accuracy may vary with facial changes
- Requires webcam access

---

## 🚀 Future Improvements

- [ ] Deep Learning-based face recognition (CNN / FaceNet)
- [ ] Web & mobile application integration
- [ ] Cloud database support
- [ ] Attendance analytics dashboard
- [ ] Liveness detection for security

---

## DEMONSTRATION VIDEO
https://drive.google.com/file/d/1FR8hu-qH3cqpljbiqzHG7uMY1RJ3Bk-f/view?usp=sharing

---

## PROJECT FILES DRIVE LINK
https://drive.google.com/drive/folders/1-DoVtcD1MkjyrnQp-lA9un7H6cEhl-d8?usp=drive_link

This Drive link contains the PPTs, Project Proposal, and Report

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests.

---

## 📄 License

This project is for educational purposes.

---

## 🙌 Acknowledgements

- [OpenCV Documentation](https://docs.opencv.org/)
- [Python Community](https://www.python.org/)
- [MySQL Documentation](https://dev.mysql.com/doc/)

---

> ⭐ If you like this project, give it a star!
