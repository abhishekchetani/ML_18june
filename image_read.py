#!/usr/bin/python

import cv2

img=cv2.imread("/home/abhishek/Desktop/tracks.jpeg")

print img
print img.shape

cv2.imshow("rail",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
