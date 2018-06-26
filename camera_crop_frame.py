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
	#cropping a portion of frame 
	crop = frame[100:200,300:400]
	#imposing cropped portion on bwimg
	temp = bwimg[100:200,300:400]	
	bwimg[100:200,300:400] = crop
	cv2.imwrite("cropped.jpg",crop)
	cv2.imwrite("temporary.jpg",temp)
	#cv2.imwrite("imposed.jpg",bwimg)
	#cv2.imshow("Edited",bwimg)
	#closing windows on pressing 'q' button	
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break

cv2.destroyAllWindows()
cap.release()
	
