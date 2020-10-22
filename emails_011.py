#!/usr/bin/env python

import sys

def name(s):
    i = 0
    for char in s:
    	if "@" in s:
    		char = char.remove(["@":])
        


        elif char[i] < "0" or char[i] > "9":
        	char = char.remove(s[i])
            i += 1

    return char

def main():
    for line in sys.stdin:
        [s] = line.strip()
        print (name(s))

if __name__ == '__main__':
	main()
