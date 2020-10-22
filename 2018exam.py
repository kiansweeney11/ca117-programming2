#!/usr/bin/env python

import sys
l = []

def count(s):
    s = sys.stdin.readlines()
    s = s.strip().split()
    count = 0
    for char in s:
        if char == "AaEe":
            count += 1
        return count

def main():
    return [s for s in l if count(s) ]


if __name__ == '__main__':
    main()
