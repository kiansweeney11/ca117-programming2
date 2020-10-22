#!/usr/bin/env python

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    def reflect(self):
        self.x = self.x * -1
        self.y = self.y * -1

    def distance(self, other):
        dist_x = other.x - self.x
        dist_y = other.y - self.y

        return (((dist_x) ** 2 + (dist_y) ** 2) ** 0.5)

from point_071 import Point

def main():
    p1 = Point()
    p2 = Point(3, 0)
    print('{:.1f}'.format(p1.distance(p2)))
    print('{:.1f}'.format(p2.distance(p1)))
    p3 = Point(3, 0)
    p3.reflect()
    print('{:.1f}'.format(p3.distance(p2)))
    p4 = Point(1, 1)
    print('{:.1f}'.format(p4.distance(p1)))

if __name__ == '__main__':
    main()
