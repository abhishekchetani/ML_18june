#!/usr/bin/python

import commands

print "****COMMANDS****"
print "1. date"
print "2. calendar"

value = raw_input("Enter your choice: ")

if value=='1':
	value1 = commands.getoutput("date")	
	print value1
elif value=='2': 
	value2 = commands.getoutput("cal")	
	print value2
else:
	print "Wrong Choice!!!"

