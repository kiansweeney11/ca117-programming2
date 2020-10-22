#!/usr/bin/env python

import sys

def anagram(a):
	a = a.strip().split(" ")
	i = 0
	if len(a[0]) != len(a[1]):
        return False
    while i < len(a[0]):
    	j = 0
    	while j < len(a[i]):
    		if a[0][i] == a[i][j]:
    			a[i] = a[i].replace(a[0][i], "", 1)
    		j += 1	
		i += 1
	if len(a[1]) == 0:
	    return True
	else:
	    return False

def main():
    if line in sys.stdin:
        print (anagram(line))

if __name__ == '__main__':
		main()
