#! /usr/bin/python

# to install opencv----command used is:-  sudo apt -get install python-opencv
#cv2 is module for python2.


import cv2

import numpy as np
#we need to give complete path of image where its stored.

img=cv2.imread("/home/q/Desktop/jon.jpeg",1)
#img1=cv2.imread("/home/q/Desktop/t.jpeg",0)
'''
imread is a function in cv2 which is used to read image passed as parameter.
color channel-- 1--> exact image i.e properties unchanged  or  cv2.IMREAD_COLOR     by default value
		0-->gray image(b/w)  or  cv2.IMREAD_BGR2GRAY
		-1-->transparent image   or  cv2.IMREAD_UNCHANGE_COLOR
  
'''



'''
#prints actual co-ordinates of image
#print("image 1 jon snow",img)
#print("image 2",img1)
#prints shape of image
#print(img.shape)

#imshow is used to show actual image-----arg1->window name   arg2-> image which is to be displayed

cv2.imshow("jon_GOT",img)
#cv2.imshow("tiryon",img1)

#waitkey is used to hold the image window  arg---- time for which we need to hold image,0->unlimited time
cv2.waitKey(0)
'''

#_______________________________________________________________________________________________________________________________________


#to draw a line in image
'''
arg1- image on which we need to draw line
arg2- start coordinate of line
arg3- end cordiante of line
arg4- BGR values of color of line
arg5- width if line
'''
cv2.line(img,(0,0),(110,130),(0,0,255),4)


#to draw rectangle in image we need 2 coordinates of diagnoal only
'''
arg1- image on which we need to draw line
arg2- start coordinate of diagonal
arg3- end cordiante of diagonal
arg4- BGR values of color of lines
arg5- width if line    #if we give -1 it will completely fill that rect with that color
'''
cv2.rectangle(img,(80,20),(150,120),(123,190,140),1)


# to draw circle in image we need center and length of radius only
cv2.circle(img,(150,50),50,(150,200,200),2)


#to make a polygon in image
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,0,255))


#to write text on image
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"classroom hiii",(10,100),font,1,(255,0,0))


#to crop a image
crop=img[20:120,80:150]
cv2.imwrite("cropped.jpeg",crop)
cv2.imshow("crop img",crop)
cv2.waitKey(0)



#imread is used to write image i.e it is used to save image
#arg1----new name of image by which we need to store it   arg2---image which we need to save
cv2.imwrite("snow.jpeg",img)


cv2.imshow("jon",img)
cv2.waitKey(0)













