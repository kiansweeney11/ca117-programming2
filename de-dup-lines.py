#!/usr/bin/env python

a = []

s = raw_input()
while s != "end":
   a.append(s)
   s = raw_input()

i = 0
p = i
j = i + 1
while i < len(a) and p[i] != j[i]:
   if p[i] == j[i]:
   
   i = i + 1

print p[i]
