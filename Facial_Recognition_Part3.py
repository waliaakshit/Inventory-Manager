import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

class ChkMe:
    def __init__(self):

        self.answer = None
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('trainer/trainer.yml')
        cascadePath = 'C:/Python/Python39/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml'
        faceCascade = cv2.CascadeClassifier(cascadePath)
        font = cv2.FONT_HERSHEY_SIMPLEX
        # initiate id counter
        id = 0

        names = ['None', 'Admin']
        # Initialize and start realtime video capture
        cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        cam.set(3, 640)  # set video widht
        cam.set(4, 480)  # set video height
        # Define min window size to be recognized as a face
        minW = 0.1 * cam.get(3)
        minH = 0.1 * cam.get(4)
        while True:
            ret, img = cam.read()

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(minW), int(minH)),
            )
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                id, confidence = recognizer.predict(gray[y:y + h, x:x + w])


                if (confidence < 100):
                    id = names[id]
                    k1 = "  {0}%".format(round(100 - confidence))
                    if (100-int(confidence))>30:
                        self.answer="yes"


                else:
                    id = "unknown"
                    k1 = "  {0}%".format(round(100 - confidence))

                cv2.putText(
                    img,
                    str(id),
                    (x + 5, y - 5),
                    font,
                    1,
                    (255, 255, 255),
                    2
                )


                display_str=self.answer
                if display_str == "yes":
                    cv2.putText(img, "Unlocked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                else:
                    cv2.putText(img, "locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

            cv2.imshow('camera', img)
            k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
            if k == 27:
                break

        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()