import cv2
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
def draw_face(img, classifier, scaleFactor, minNeighbors, color, text):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
    coords = []
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 3)
        cv2.putText(img, text, (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1)
    return img

def detect(img, faceCascade):
    img = draw_face(img, faceCascade, 1.1, 10, (0, 0, 255), "Face")
    return img

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = detect(frame, faceCascade)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

