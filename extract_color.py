#!/usr/bin/python

import cv2
import time

img = cv2.imread("Heels.jpg")
grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#print height & width
print img.shape

#pause for 2 seconds
#time.sleep(2) 

#print matrix
print img

#time.sleep(2)

#check for red colour & extract it
redheels = cv2.inRange(img,(0,0,0),(40,40,255))
cv2.imshow("original",img)
cv2.imshow("onlyred",redheels)
cv2.imwrite("Extracted.jpg",redheels)

'''
show red part in red only
new = cv2.bitwise_and(img,redheels)
cv2.imshow("newred",new)
'''

cv2.waitKey(0)
cv2.destroyAllWindows()

