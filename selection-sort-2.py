#!/usr/bin/env python

a = []

s = raw_input()
while s != "end":
   a.append(int(s))
   s = raw_input()

p = input()
j = p + 1
while j < len(a):
   if a[j] < a[p]:
      p = j
   j = j + 1

print p
