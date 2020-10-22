#!/usr/bin/env python

a = []
s = raw_input()

while s != "end":
   a.append(s)
   s = raw_input()

n = len(a)

i = 0
while i < len(a):
   print i, n, a[i]
   i = i + 1
