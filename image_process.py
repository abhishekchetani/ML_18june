#!/usr/bin/python

import cv2

img1 = cv2.imread("/home/abhishek/Desktop/tracks.jpeg",1)
img2 = cv2.imread("/home/abhishek/Desktop/tracks.jpeg",0)
img3 = cv2.imread("/home/abhishek/Desktop/tracks.jpeg",-1)

print img1.shape
print img2.shape
print img3.shape

cv2.imshow("original",img1)
cv2.imshow("bwimg",img2)
cv2.imshow("transparent",img3)

cv2.imwrite("/home/abhishek/Desktop/grayimg.jpeg",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

