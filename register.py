import cv2
import os
from database import connect_db

def register_user(user_id, name):

    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (id, name) VALUES (%s, %s)", (user_id, name))
    conn.commit()
    conn.close()

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    count = 0

    if not os.path.exists("dataset"):
        os.makedirs("dataset")

    while True:
        ret, img = cam.read()
        if not ret:
            print("Camera error")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            count += 1
            cv2.imwrite(f"dataset/User.{user_id}.{count}.jpg", gray[y:y+h, x:x+w])
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.imshow('Register Face', img)

        if cv2.waitKey(1) == 27 or count >= 50:
            break

    cam.release()
    cv2.destroyAllWindows()

    print("User Registered Successfully!")