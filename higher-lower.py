#!/usr/bin/env python

curr = input()
prev = curr
while curr != prev:
   if prev < curr:
      print "higher"
   elif prev > curr:
      print "lower"
   else:
      print "equal"
   prev = curr
   curr = input()
