#!/usr/bin/env python

import sys

def palindrome(a):
	a = a.strip().lower()
	i = 0
	for char in a:
		if not char.isalnum():
			a = a.replace(char, "", 1)
		i += 1
		
		s = a[::-1]
		if a == s:
		    return True
		else:
		    return False

def main():
    for line in sys.stdin:
        print (palindrome(line))

if __name__ == '__main__':
		main()
