#!/usr/bin/env python

import sys
N = int(sys.argv[1])
l = [n for n in range(1, N + 1)]

def mul3(l):
	return [n for n in l if n % 3 == 0]

def square3(l, N):
	return [n ** 2 for n in l if n % 3 == 0]

def doublemul4(l, N):
	return [n * 2 for n in l if n % 4 == 0]

def mulor(l, N):
	return [n for n in l if n % 3 == 0 or n % 4 == 0]

def mulx2(l, N):
	return [n for n in l if n % 3 == 0 and n % 4 == 0]

def mul3replace(l, N):
	return ["X" if n % 3 == 0 else n for n in l]

def is_prime(x):
	if x == 1:
		return False
	for i in range(2, x // 2 + 1):
		if x % i == 0:
			return False
	return True

def prime_number(l, N):
    return [n for n in range(1, N + 1) if is_prime(n)]

print ("Multiples of 3: {}".format(mul3(l)))
print ("Multiples of 3 squared: {}".format(square3(l, N)))
print ("Multiples of 4 doubled: {}".format(doublemul4(l, N)))
print ("Multiples of 3 or 4: {}".format(mulor(l, N)))
print ("Multiples of 3 and 4: {}".format(mulx2(l, N)))
print ("Multiples of 3 replaced: {}".format(mul3replace(l, N)))
print ("Primes: {}".format(prime_number(l, N)))
