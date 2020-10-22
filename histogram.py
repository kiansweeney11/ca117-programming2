#!/usr/bin/env python

a = []

s = raw_input()
while s != "end":
   a.append(int(s))
   s = raw_input()

i = 0
count = 0
while i < len(a) and "0" <= a[i] and a[i] <= "9":
   j = i + 1
   if a[i] = a[j]:
      count = count + 1

print a(i), count "*"
