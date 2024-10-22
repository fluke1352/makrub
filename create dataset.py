"""ไฟล์ืสร้างฐานข้อมูล create dataset"""
#ไฟล์สร้างภาพถ่ายบุคคล และ ระบุเลขประจำตัวนักศึกษาเป็นชื่อไฟล์ เพื่อเก็บเป็น data
import cv2
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def dataset(img, id, img_id):
    """สร้างไฟล์รูปภาพเก็บไว้ในโฟลเดอร์"""
    cv2.imwrite("data/stid."+str(id)+"."+str(img_id)+".jpg", img) # data is firename you can change

def draw_object(img, classifier, scaleFactor, minNeighbors, color):
    """สร้างกรอบรูปเพื่อแสดงกรอบการตรวจจับใบหน้า ตอนถ่ายภายบุคคล"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
    position = []
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 3)
        cv2.putText(img, str(img_id), (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1)
        position = [x,y,w,h]
    return img, position

def detect(img, faceCascade, img_id):
    """สร้างชื่อไฟล์ของรูปภาพขณะถ่าย (รหัสนักศึกษา)"""
    #หลังจากเลขนักศึกษา จะมีเลขจำนวนรูปที่ถ่าย
    img, position = draw_object(img, faceCascade, 1.1, 10, (0, 0, 0))
    if len(position) == 4:
        id = 62070171 # XXX = studenID you can use for loop auto run studenID
        cut_face = img[position[1]:position[1]+position[3], position[0]:position[0]+position[2]]
        dataset(cut_face, id, img_id)
    return img

img_id = 0
cap = cv2.VideoCapture(0)#XXX = studenID you can use for loop auto run studenID

while True:
    """เปิดลูปการถ่ายรูปจนกว่าจะกดหยุด ตั้งค่าให้กดปุ่ม q เพื่อหยุดถ่าย"""
    ret, frame = cap.read()
    frame = detect(frame, faceCascade, img_id)
    cv2.imshow('frame', frame)
    img_id += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        create(member)
        break

cap.release()
cv2.destroyAllWindows()
