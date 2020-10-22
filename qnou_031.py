#!/usr/bin/env python

import sys
def main():
    l = []
    for word in sys.stdin:
        if "q" in word.lower():
            if word.lower().count("qu") != word.lower().count("q"):
                l.append(word.strip())
    print ("Words with q but no u: {}".format(l))

if __name__ == '__main__':
    main()
