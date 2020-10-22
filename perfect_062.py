 #!/usr/bin/env python

import sys
 
def sumFac(n):
    a = []
    #divisible = 0
    for i in range(1, n // 2 + 1):
        if int(n) % int(i) == 0:
            a.append(i)
        return a
 
def isPerfect(n):
    if sum(sumFac(n)) == n:
        return True
    else:
        return False
 
def main():
    for n in sys.stdin:
        print (isPerfect(int(n))



if __name__ == '__main__':
    main()
