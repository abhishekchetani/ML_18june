#!/usr/bin/python

import cv2
import time 

#doing bitwise AND operation on camera frames for detecting motion (change in bits)
def frames_diff(x,y,z):
	img1 = cv2.absdiff(x,y)
	img2 = cv2.absdiff(y,z)
	comm_diff = cv2.bitwise_and(img1,img2)
	return comm_diff

#opening the camera
cap = cv2.VideoCapture(0)

#capturing 3 consistent frames
frame1 = cap.read()[1]
frame2 = cap.read()[1]
frame3 = cap.read()[1]

#converting to grayscale
gray1 = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(frame3,cv2.COLOR_BGR2GRAY)

while cap.isOpened():
	
	'''
	img1 = cv2.absdiff(gray1,gray2)
	img2 = cv2.absdiff(gray2,gray3)
	comm_diff = cv2.bitwise_and(img1,img2)	
	'''

	imgdiff = frames_diff(gray1,gray2,gray3)
	#cv2.imshow("Motion Detector",comm_diff)	
	cv2.imshow("Motion Detector",imgdiff)
	
	#taking 3 subsequent frames for further processing
	status,frame = cap.read()
	gray1 = gray2
	gray2 = gray3
	gray3 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	
	#waiting for user to terminate program
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break

cv2.destroyAllWindows()
cap.release()	
	
