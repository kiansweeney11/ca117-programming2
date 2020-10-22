#!/usr/bin/env python

import sys

class Stack():

	def __init__(self):
		self.l = []

	def push(self, e):
		self.l.append(e)

	def pop(self):
		return self.l.pop()

class Queue(object):

	def __init__(self):
		self.l = []

	def enqueue(self, e):
		self.l.append(e)

	def dequeue(self):
		return self.l.pop(0)

	def __len__(self):
		return len(self.l)

def isfloat(num):
	try:
		float(num)
	except ValueError:
		return False

	return True

def calculator(line):
	num = Stack()
	op = Queue()

	line = line.split()
	i = 0
	while i < len(line) and isfloat(line[i]):
		num.push(float(line[i]))
		i += 1

	while i < len(line):
		op.enqueue(line[i])
		i += 1

	while len(op) > 0:
		operation = op.dequeue()
		num1 = num.pop()

		if operation.isalpha():
			if operation == 'r':
				num.push(num1 ** (1/2))
			else:
				num.push(num1 * -1) 

		else:
			num2 = num.pop()
			new_num = eval(str(num2) + operation + str(num1))
			num.push(new_num)

	return num.pop()

def main():

    for line in sys.stdin:
        try:
            a = calculator(line.strip())
            print('{:.2f}'.format(a))
        except IndexError:
            print('Invalid RPN expression')

if __name__ == '__main__':
    main()
