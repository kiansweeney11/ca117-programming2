#!/usr/bin/env python

class P(object):
    
    z = 99
    
    def __init__(self, a=1):
        self.a = a

    def foo(self):
        return 'green'

class Q(P):
    
    z = 98
    
    def __init__(self, a, b=2):
        super().__init__(a)
        self.b = b

    def foo(self):
        return 'orange'

class R(P):
    
    x = 99
    
    def __init__(self, a, b, c=3):
        super().__init__(a)
        self.b = b
        self.c = c

    def moo(self):
        return 'purple'

class S(R):
    
    def __init__(self, a, b, c, d=4):
        super().__init__(a, b, c)
        self.d = d


q = Q(10)
s = S(13, 14, 15)


print('A: {}'.format(q.a))
print('B: {}'.format(q.b))
print('C: {}'.format(s.d))
print('D: {}'.format(s.z))
print('E: {}'.format(s.foo()))
print('F: {}'.format(q.moo()))
