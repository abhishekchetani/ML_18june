#!/usr/bin/python

import time
print "Hello"
time.sleep(2)
var1 = input("Enter 1st element of list:")
var2 = input("Enter 2nd element of list:")
var3 = input("Enter 3rd element of list:")
var4 = input("Enter 4th element of list:")
time.sleep(2)
print var1, var2, var3, var4
time.sleep(2)
x = [var1,var2,var3,var4]
print x
time.sleep(2)
print "1st element of list: ",x[0]
print "2nd element of list: ",x[1]
print "3rd element of list: ",x[2]
print "4th element of list: ",x[3]
time.sleep(2)
print "Type of x = ",type(x)
