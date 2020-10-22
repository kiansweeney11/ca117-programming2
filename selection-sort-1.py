#!/usr/bin/env python

a = []

s = raw_input()
while s != "end":
   a.append(int(s))
   s = raw_input()

i = 1
p = 0
while i < len(a):
   if a[i] < a[p]:
   	  p = i
   i = i + 1
  
print p
 