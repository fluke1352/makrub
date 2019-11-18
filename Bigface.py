import cv2
import xlsxwriter
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
member = set()

def draw_object(img, classifier, scaleFactor, minNeighbors, color, clf):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
    position = []
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 3)
        id,confidet = clf.predict(gray[y:y+h, x:x+w])

        if -20 <= confidet <= 100:
            cv2.putText(img, str(id), (x,y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
            member.add(id)
        else:
            cv2.putText(img, "unknow", (x,y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        position = [x,y,w,h]
    return img, position

def detect(img, faceCascade, img_id, clf):
    img, position = draw_object(img, faceCascade, 1.1, 10, (0, 0, 255), clf)
    if len(position) == 4:
        # id = 62070
        cut_face = img[position[1]:position[1]+position[3], position[0]:position[0]+position[2]]
    return img

def create(member):
    """create exceil fire"""
    member_ = xlsxwriter.Workbook('member.xlsx')
    worksheet = member_.add_worksheet()
    member = list(member)
    member.sort()
    row = 0
    column = 0
    for i in member:
        worksheet.write(row, column, i)
        row += 1
    member_.close()

img_id = 1
camera = cv2.VideoCapture(0)

clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("classifier.xml")

while True:
    ret, frame = camera.read()
    frame = detect(frame, faceCascade, img_id, clf)
    cv2.imshow('frame', frame)
    img_id += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(member)
        create(member)
        break
camera.release()
cv2.destroyAllWindows()
