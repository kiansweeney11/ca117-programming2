#!/usr/bin/env python

i = 1
while i < len(a) and a[i] != "end":
   v = a[i]
   p = i
   while 0 < p and v < a[p-1]:
      a[p] = a[p-1]
      p = p - 1
   a[p] = v

   i = i + 1


