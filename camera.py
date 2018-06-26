#!/usr/bin/python

import cv2

#enabling the camera
cap = cv2.VideoCapture(0)

#checking for proper functioning of camera
if cap.isOpened():
        print "camera is working"
        status,frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",frame)
	cv2.imshow("grayimg",gray)
	#destroy all windows on press of any button        
	cv2.waitKey(0)   
        cv2.destroyAllWindows()
else:
    print "drivers not installed"

#disabling the camera
cap.release()

