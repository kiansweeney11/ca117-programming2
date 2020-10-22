#!/usr/bin/env python

i = 0 
s = raw_input()

while i < len(s):
   total = 0
   while i < len(s) and s[i] != "+"
      i = i + 1
   num1 = int(s[0:i])
   i = i + 1
   num2 = + int(s[i:])
   total = num1 + num2
   print total
   if total != 1000:
   	  i = 0
   	  s = raw_input()
   else:
   	  i = len(s)
