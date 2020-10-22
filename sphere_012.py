#!/usr/bin/env python

import sys
import math

def math():
	i = start_r
	while i <= end_r:
	    Radius = i
        Area = 4 * math.pi * radius^2
        Volume = (4 * math.pi * Radius^3)/ 3.0
        print ("{:>10.1f} {:>15.2f} {:>15.2f}".format(radius, area, volume))
	i += inc_r

def main():
    start_r = float(sys.argv[1])
    inc_r = float(sys.argv[2])
    end_r = float(sys.argv[3])
    table_r(start_r, inc_r, end_r)

    h1 = 'Radius (m)'
    h4 = '-' * len(h1)
    h2 = 'Area (m^2)'
    h5 = '-' * len(h2)
    h3 = 'Volume (m^3)'
    h6 = '-' * len(h3)

    print('{:>s} {:>15s} {:>15s}'.format(h1, h2, h3))
    print('{:>s} {:>15s} {:>15s}'.format(h4, h5, h6))

if __name__ == '__main__':
    main()
