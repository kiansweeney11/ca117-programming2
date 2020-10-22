#!/usr/bin/env python

import sys
import calendar

def main():
    yearb = int(sys.argv[3])
    monthb = int(sys.argv[2])
    dayb = int(sys.argv[1])
    day_week = calendar.weekday(yearb, monthb, dayb)
#    print (birthday(day_week))
    a = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    b = ["Monday's child is fair of face", "Tuesday's child is full of grace", "Wednesday's child is full of woe", "Thursday's child has far to go", "Friday's child is loving and giving", "Saturday's child works hard for a living", "Sunday's child is fair and wise and good in every way"]
    print ("You were born on a {} and {}.".format(a[day_week], b[day_week]))

if __name__ == '__main__':
    main()
