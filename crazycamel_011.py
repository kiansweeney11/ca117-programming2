#!/usr/bin/env python

import sys

def crazy(s):
    newline = " "
    for word in s:
        word = word[0:-1] + word[-1].upper()
        newline = newline + " " + word
    return newline.strip()

def main():
    lines = sys.stdin.readlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip().split()
        print (crazy(line))
        i += 1

if __name__ == '__main__':
    main()
