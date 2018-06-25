#!/usr/bin/python

import cv2

img = cv2.imread("/home/abhishek/Desktop/tracks.jpeg")

cv2.line(img,(0,0),(236,236),(100,54,255),3)
cv2.rectangle(img,(199,112),(325,238),(0,0,255),2)
cv2.circle(img,(262,175),60,(255,200,0),3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'TRAIN',(210,270),font,1,(90,200,140),cv2.LINE_4)

cv2.imshow("actions",img)
cv2.imwrite("/home/abhishek/Desktop/lines.jpeg",img)

cv2.waitKey(0)      
cv2.destroyAllWindows()
                       
