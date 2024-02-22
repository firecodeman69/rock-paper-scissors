import cv2

capture = cv2.VideoCapture(0)
ret, frame = capture.read()
capture.release()
cv2.imwrite("playerchoice.jpg", frame)