#!/usr/bin/env python

import sys

def main():
    lines = sys.stdin.readlines()
    try:
        i = 0
        z = []
        for line in lines:
            try:
                line = lines[i].strip().split()
                p = max_power(line)
                list1 = (ssd(p, line))
                #print(max_power)
                print(math(list1))

            except ValueError:
                z.append(i)
                #print (z)
            i += 1

    finally:
        if len(z) > 0:
            m = []
            j = 0
            while j < len(z):
                m.append(str(z[j] + 1))
                j += 1
            print ("Failed to convert line(s): " + ", ".join(m) + " ")

def max_power(s):
    number = int(s[0])
    base = int(s[1])
    i = 0
    while base ** i < number:
        i += 1
    return i - 1

def ssd(p, s):
    number = int(s[0])
    base = int(s[1])
    a = []
    i = 0
    while i <= p:
        z = (number // (base ** (p - i)))
        a.append(int(z))
        number = (number - ((base ** (p - i)) * z))
        i = i + 1
    return a

def math(x):
    sum_squares = 0
    i = 0
    while i < len(x):
        p = int(x[i]) ** 2
        sum_squares = p + sum_squares
        i += 1
    return sum_squares


if __name__ == '__main__':
    main()
