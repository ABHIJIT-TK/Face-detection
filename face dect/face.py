import cv2
from random import randrange

trained_face_data=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

#img=cv2.imread('RDJ.png')

webcam=cv2.VideoCapture(0)
# in camera
while True:
    successful_frame,frame=webcam.read()
    grayscale_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_coordinates=trained_face_data.detectMultiScale(grayscale_img)
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0 ,255,0),2)
    cv2.imshow('img',frame)
    key=cv2.waitKey(1)
    
    #TO STOP
    if key==81 or key==113:
        break
webcam.release()
#grayscale_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
"""
face_coordinates=trained_face_data.detectMultiScale(grayscale_img)

#print(face_coordinates)

for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0 ,255,0),2)

cv2.imshow('image',img) 

cv2.waitKey()
"""