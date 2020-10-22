#!/usr/bin/env python

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    def midpoint(self, other):
        midx = (self.x + other.x) / 2
        midy = (self.y + other.y) / 2
        return (Point(midx, midy))

    def __str__(self):
        return ('{:.1f}, {:.1f}'.format(self.x, self.y))

class Circle(object):

    def __init__(self, radius=0.0, centre=Point(0, 0)):
        self.radius = radius
        self.centre = centre

    def __add__(self, other):
        centre = Point.midpoint(self.centre, other.centre)
        radius = self.radius + other.radius
        return Circle(radius, centre)

    def __str__(self):
        l = []
        l.append('Centre: ({:.1f}, {:.1f})'.format(self.radius))
        l.append('Radius: {}'.format(self.centre))
        return '\n'.join(l)

def main():
    p1 = Point()
    p2 = Point(4, 6)
    c1 = Circle(p1, 10)
    c2 = Circle(p2, 5)
    c3 = c1 + c2
    print(c3)

    p3 = Point(10, 10)
    c4 = Circle(p3, 15)
    c5 = c2 + c4
    print(c5)

if __name__ == '__main__':
    main()
