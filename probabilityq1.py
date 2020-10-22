#!/usr/bin/env python
'''
from scipy.stats import binom

binom.pmf(k) = choose(n, k) * p ** k * (1 - p) ** (n - k)
'''
from scipy.stats import binom

n = [10, 50, 100, 500, 1000, 5000]

p = [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 0.5, 0.7, 0.9, 0.99, 0.999]

binom.pmf(k) = choose(n, k) * p ** k * (1 - p) ** (n - k)
