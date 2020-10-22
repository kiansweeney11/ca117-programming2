#!/usr/bin/env python

import sys

def main():
    l = []
    for line in sys.stdin:
        l.append(line.strip())

    i = 0
    while i < len(l):
        if l[i].isdigit():
            print ("Thank you for {:}".format(l[i]))
            i = len(l)
        else:
            print ("{:} is not a number".format(l[i]))
        i += 1


if __name__ == '__main__':
    main()
