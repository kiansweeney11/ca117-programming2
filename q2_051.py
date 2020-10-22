#!/usr/bin/env python

import sys

def func(s):
    word = str(s).lower()
    string = "evil"
    for char in word:
        if char not in string:
            word = word.replace(char, "")
    if word == string:
        return("".join(s))
    else:
        return ""

def main():
    lines = sys.stdin.readlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip().split()
        a = []
        a.append(func(line))
        if a[0] != "":
            print ("".join(a))
        i += 1

if __name__ == '__main__':
    main()
