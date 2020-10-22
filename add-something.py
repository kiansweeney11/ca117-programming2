#!/usr/bin/env python

a = []

m = raw_input()
while m != "end":
   a.append(int(m))
   m = raw_input()

n = input()
i = 0
while i < len(a):
   a[i] = a[i] + n
   print a[i]
   i = i + 1
