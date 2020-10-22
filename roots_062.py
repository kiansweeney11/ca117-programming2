#!/usr/bin/env python

import sys

def roots(a, b, c):
    if ((b ** 2) - 4 * a * c) < 0:
        print (None)
    else:
        r1 = (-b + ((b ** 2) - 4 * a * c) ** 0.5) / (2 * a)
        r2 = (-b - ((b ** 2) - 4 * a * c) ** 0.5) / (2 * a)
        print ("r1 = {}, r2 = {}".format(float(r1), float(r2)))

def main():
    a = [l.strip().split() for l in sys.stdin]
    for line in a:
        roots(float(line[0]), float(line[1]), float(line[2]))

if __name__ == '__main__':
    main()
