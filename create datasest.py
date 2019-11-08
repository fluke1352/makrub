import cv2
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def dataset(img, id, img_id):
    cv2.imwrite("data/stid."+str(id)+"."+str(img_id)+".jpg", img) # data is firename you can change

def draw_object(img, classifier, scaleFactor, minNeighbors, color):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
    position = []
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 3)
        cv2.putText(img, str(img_id), (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1)
        position = [x,y,w,h]
    return img, position

def detect(img, faceCascade, img_id):
    img, position = draw_object(img, faceCascade, 1.1, 10, (0, 0, 0))
    if len(position) == 4:
        id = 62070061 # XXX = studenID you can use for loop auto run studenID
        cut_face = img[position[1]:position[1]+position[3], position[0]:position[0]+position[2]]
        dataset(cut_face, id, img_id)
    return img

img_id = 0
cap = cv2.VideoCapture("62070061.jpg")#XXX = studenID you can use for loop auto run studenID

# while True:
ret, frame = cap.read()
frame = detect(frame, faceCascade, img_id)

cap.release()
cv2.destroyAllWindows()