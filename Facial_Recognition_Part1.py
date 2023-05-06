import cv2
import numpy as np
import os
from PIL import Image

detector= cv2.CascadeClassifier('C:/Python/Python39/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
class CreateDataset:

    def __init__(self):
        face_detector = cv2.CascadeClassifier('C:/Python/Python39/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

        face_id=1
        cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        cam.set(3, 640) # set video width
        cam.set(4, 480) # set video height

        count = 0
        while(True):
            ret, img = cam.read()

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
                count += 1
                # Save the captured image into the datasets folder
                file_name_path = 'C:/Users/lenovo/PycharmProject/MOBIretail/faces/user.' + str(face_id) + '.' + str(count) + '.jpg'
                cv2.imwrite(file_name_path, gray[y:y+h,x:x+w])
                cv2.imshow('image', img)
            k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break
            elif count >= 100:
                 break

        cam.release()
        cv2.destroyAllWindows()

        #traiinig of the data is basically conisdered to be done at this point
        # Path for face image database
        path = 'C:/Users/lenovo/PycharmProject/MOBIretail/faces'
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        print("\n [INFO] Training faces. It will take a few seconds. Wait ...")
        faces, ids = self.getImagesAndLabels(path)

        recognizer.train(faces, np.array(ids))
        # Save the model into trainer/trainer.yml
        recognizer.write('trainer/trainer.yml')

        print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))


    def getImagesAndLabels(self,path):
        global detector
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        ids = []
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L')  # grayscale
            img_numpy = np.array(PIL_img, 'uint8')
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)
            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y + h, x:x + w])
                ids.append(id)
        return faceSamples, ids

