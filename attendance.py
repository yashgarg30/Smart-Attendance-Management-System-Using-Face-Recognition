import cv2
import datetime
import json
from database import connect_db

def start_attendance():

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')

    # load label map
    with open("trainer/labels.json", "r") as f:
        label_map = json.load(f)

    reverse_map = {v:k for k,v in label_map.items()}

    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    conn = connect_db()
    cursor = conn.cursor()

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    marked_ids = set()

    while True:
        ret, img = cam.read()

        if not ret:
            print("Camera error")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)

        for (x,y,w,h) in faces:

            label, confidence = recognizer.predict(gray[y:y+h,x:x+w])

            if confidence < 70:

                student_id = reverse_map.get(label, None)

                if student_id:

                    cursor.execute("SELECT name FROM students WHERE id=%s", (student_id,))
                    result = cursor.fetchone()

                    if result:
                        name = result[0]

                        if student_id not in marked_ids:

                            now = datetime.datetime.now()
                            date = now.strftime("%Y-%m-%d")
                            time = now.strftime("%H:%M:%S")

                            cursor.execute(
                                "INSERT INTO attendance (id, name, date, time) VALUES (%s,%s,%s,%s)",
                                (student_id, name, date, time)
                            )
                            conn.commit()

                            marked_ids.add(student_id)

                        label_text = f"{student_id} - {name}"

                    else:
                        label_text = "Unknown"

                else:
                    label_text = "Unknown"

            else:
                label_text = "Unknown"

            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img,label_text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)

        cv2.imshow('Attendance System', img)

        if cv2.waitKey(1) == 27:
            break

    cam.release()
    cv2.destroyAllWindows()
    conn.close()