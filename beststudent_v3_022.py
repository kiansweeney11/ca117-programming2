#!/usr/bin/env python

import sys

def main():
    try:
        file = sys.argv[1]
        with open(file, "r") as f:
            f = f.readlines()
            highest = 0
            for line in f:
                try:
                    line = line.strip().split()
                    result = int(line[0])
                    line[1:] = [" ".join(line[1:])]
                    if highest < result:
                        highest = result
                        name = line[1]

                except(ValueError):
                    print ("Invalid mark {:s} encountered. Skipping.".format(line[0]))
    except(IOError):
        print ("The file {:s} could not be opened.".format(f))

    print ("Best student: {}".format(name))
    print ("Best mark: {}".format(highest))

if __name__ == '__main__':
    main()
