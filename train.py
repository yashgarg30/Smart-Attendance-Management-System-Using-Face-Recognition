import cv2
import numpy as np
from PIL import Image
import os
import json

def train_model():

    path = 'dataset'
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    faceSamples = []
    ids = []

    label_map = {}
    current_label = 0

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]

    for imagePath in imagePaths:

        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img,'uint8')

        student_id = os.path.split(imagePath)[-1].split(".")[1]

        if student_id not in label_map:
            label_map[student_id] = current_label
            current_label += 1

        label = label_map[student_id]

        faces = detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(label)

    if len(faceSamples) == 0:
        print("No faces found. Training skipped.")
        return

    recognizer.train(faceSamples, np.array(ids))

    if not os.path.exists("trainer"):
        os.makedirs("trainer")

    recognizer.save("trainer/trainer.yml")

    # save label map
    with open("trainer/labels.json", "w") as f:
        json.dump(label_map, f)

    print("Training Complete!")