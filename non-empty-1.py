#!/usr/bin/env python

if __name__ == "__main__":
    a = ["", "", "dog", "", "", "cat", "", "", "", "mouse"]

i = 0
while i < len(a) and a[i] == "":
    print int(a[i])
    i = i + 1
