#!/usr/bin/python

def factorial(num):
	if(num==1):
		return num
	else:
		return num*factorial(num-1)

num = input("Enter number: ")

if num<0:
	print "Factorial does not exist for a negative number"
elif num==0:
	print "Factorial = 1"
else:
	print "Factorial of ",num," is: ",factorial(num)

