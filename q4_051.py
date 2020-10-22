#!/usr/bin/env python

import sys

def main():
    nums = [int(line.strip()) for line in sys.stdin]

    N = len(nums)
    total = sum(nums)

    mean = total / N
    snums = sorted(nums)
    if N % 2:
        median = snums[N // 2]
    else:
        median = (snums[N // 2 - 1] + snums[N // 2]) / 2

    print('Mean: {:.1f}'.format(mean))
    print('Median: {:.1f}'.format(median))

if __name__ == '__main__':
    main()
