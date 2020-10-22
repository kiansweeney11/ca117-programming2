#!/usr/bin/env python

n = raw_input()

i = 0
while i < len(n):
   p = i
   j = i + 1
   while j < len(n):
      if a[j] = a[p]:
         p = j
         j = j + 1

   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp

   i = i + 1

print int(n)
