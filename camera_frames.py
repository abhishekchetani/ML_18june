#!/usr/bin/python

import cv2
import random

cap = cv2.VideoCapture(0)

while cap.isOpened():
	#print "camera is working"
	#capturing frames	
	status,frame = cap.read()
	#converting to grayscale	
	bwimg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	#drawing rectangles	
	cv2.rectangle(frame,(100,100),(200,200),(255,0,0),3)
	cv2.rectangle(frame,(100,250),(200,350),(255,0,0),3)
	cv2.rectangle(frame,(300,100),(400,200),(255,0,0),3)
	cv2.rectangle(frame,(300,250),(400,350),(255,0,0),3)
	#putting text on frame	
	font = cv2.FONT_HERSHEY_SIMPLEX	
	cv2.putText(bwimg,'Written Text',(70,70),font,2,(70,0,255),cv2.LINE_4)	
	#displaying camera frames	
	cv2.imshow("camera1",frame)
	cv2.imshow("camera2",bwimg)
	#generating random nos. for saving frames	
	x = random.random()
	y = str(x)[2:5]
	cv2.imwrite("abhishek"+y+".jpg",frame)
	#closing windows on pressing 'q' button	
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break

cv2.destroyAllWindows()
cap.release()
	
