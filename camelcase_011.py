#!/usr/bin/env python

import sys

def firstcap(s):
	newline = " "
	for word in s:
		newline = newline + " " + word.capitalize()
	return newline.strip()

def main():
	lines = sys.stdin.readlines()
	i = 0
	while i < len(lines):
		line = lines[i].strip().split()
		print (firstcap(line))
		i += 1

if __name__ == '__main__':
	main()
