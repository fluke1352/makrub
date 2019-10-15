import cv2

img = cv2.imread('sony.jpg',1)
img = cv2.line(img, (0, 0), (255, 255), (0,0, 255), 10)#(pictuer, (start), (stop), (color(blue,green,red)), thick)
img = cv2.arrowedLine(img, (0, 0), (400, 400), (0, 200, 255), 5)#(pictuer, (start), (stop), (color(blue,green,red)), thick)
img = cv2.rectangle(img, (350,0), (500, 120), (200, 0, 200), 5)#(pictuer, (start), (stop), (color(blue,green,red)), thick)
img = cv2.circle(img, (450, 100), 50, (100, 0, 0), 5)#pictuer, (center), (radius), (cloor), thick if thick = -1 fillcolor)
img = cv2.putText(img, "Fluke", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
cv2.imshow('sony',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.imwrite("sony2.png", img)

# lis = []
# cap = cv2.VideoCapture(0)#0 = camara if another ,vedeo or picture
# while True:
#     ret, frame = cap.read()
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()