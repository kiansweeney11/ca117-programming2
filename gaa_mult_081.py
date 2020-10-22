#!/usr/bin/env python

class Score(object):

    def __init__(self, goal=0, point=0):
        self.goal = goal
        self.point = point

    def __str__(self):
        return ("{} goals and {} point(s)".format(self.goal, self.point))

    def __eq__(self, other):
        return (self.goal * 3) + self.point == (other.goal * 3) + other.point

    def __gt__(self, other):
        return (self.goal * 3) + self.point > (other.goal * 3) + other.point

    def __lt__(self, other):
        return (self.goal * 3) + self.point < (other.goal * 3) + other.point

    def __ge__(self, other):
        return (self.goal * 3) + self.point >= (other.goal * 3) + other.point

    def __le__(self, other):
        return (self.goal * 3) + self.point <= (other.goal * 3) + other.point

    def __add__(self, other):
        return Score(self.goal + other.goal, self.point + other.point)

    def __sub__(self, other):
        return Score(self.goal - other.goal, self.point - other.point)

    def __iadd__(self, other):
        self.goal += other.goal
        self.point += other.point
        return self

    def __isub__(self, other):
        self.goal -= other.goal
        self.point -= other.point
        return self

    def __mul__(self, n):
        self.goal = self.goal * int(n)
        self.point = self.point * int(n)
        return Score(self.goal, self.point)

    def __rmul__(self, n):
        self.goal *= n
        self.point *= n
        return Score(self.goal, self.point)

    def __imul__(self, n):
        self.goal *= n
        self.point *= n

        return self

    def __str__(self):
        return ("{} goal(s) and {} point(s)".format(int(self.goal), int(self.point)))

from gaa_mult_081 import Score

def main():

    # Create some instances of Score
    s1 = Score()
    s2 = Score(3, 12)
    s3 = Score(4, 9)
    s4 = Score(2, 11)
    s5 = Score(1, 1)

    # Display
    print('Display...')
    print(s1)
    print(s2)
    print(s3)
    print(s4)

    # Multiplication
    print('Multiplication...')
    s2 = s2 * 2
    print(s2)
    print(s2 > s3)

    # Right multiplication
    print('Right multiplication...')
    s2 = 2 * s2
    print(s2)
    print(s2 > s3)

    # In-place multiplication
    print('In-place multiplication...')
    s2alias = s2
    s2 *= 2
    print(s2)
    print(s2alias)
    print(s2 == s2alias)

if __name__ == '__main__':
    main()
