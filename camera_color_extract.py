#!/usr/bin/python

import cv2
import time

cap = cv2.VideoCapture(0)

while cap.isOpened():
	status,frame = cap.read()
	
	#check for diff colours & extract it
	onlyblue = cv2.inRange(frame,(0,0,0),(255,10,10))
	onlyred = cv2.inRange(frame,(0,0,0),(10,10,255))
	onlygreen = cv2.inRange(frame,(0,0,0),(10,255,10))	
	
	#cv2.imshow("original",frame)
	cv2.imshow("onlyred",onlyred)
	#cv2.imshow("onlyblue",onlyblue)
	#cv2.imshow("onlygreen",onlygreen)
	
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break

cv2.destroyAllWindows()
cap.release()

