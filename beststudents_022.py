#!/usr/bin/env python

import sys

def main():
    try:
        file = sys.argv[1]
        with open(file, "r") as f:
            f = f.readlines()
            highest = -1
            for line in f:
                try:
                    line = line.strip().split()
                    result = int(line[0])
                    s = " ".join(line[1:])
                    name = s
                    if highest < result:
                        highest = result
                        topstus = name
                    elif result == highest:
                        topstus = topstus + ", " + name

                except(ValueError):
                    print ("Invalid mark {:s} encountered. Skipping.".format(line[0]))

    except(IOError):
        print ("The file {:s} could not be opened.".format(f))

    print("Best student(s): {}".format(topstus))
    print("Best mark: {}".format(highest))


if __name__ == '__main__':
    main()
