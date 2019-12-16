import numpy as np #pip install numpy
from PIL import Image #pip install Pillow
import os
import cv2 #pip install opencv-python
#pip install opencv-contrib-python

def train(data):
    """สร้างลิสมาเพื่อเก็บข้อมูล"""
    path = [os.path.join(data, i) for i in os.listdir(data)]
    face = []
    id_ = []

    for icon in path:
        """สร้างลูปมาเพื่อเปลี่ยนไฟล์ภาพเป็นไฟล์.xmlเพื่อเปรียบเทียบหน้าคน"""
        img = Image.open(icon).convert("L")
        iconNp = np.array(img, "uint8")
        id = int(os.path.split(icon)[1].split(".")[1])#cut .jpg
        face.append(iconNp)
        id_.append(id)
    id_ = np.array(id_)
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(face,id_)
    clf.write("classifier.xml")


train("data")
