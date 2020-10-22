#!/usr/bin/env python

import sys

def main():
    for line in sys.stdin:
        uppers = ''.join([c if c.isupper() else '0' for c in line.strip()])
        tokens = uppers.split('0')
        print(max(tokens, key=len))

if __name__ == '__main__':
    main()
