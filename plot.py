#!/usr/bin/env python

"""
Simulates printing a bar graph.
"""

import sys
import time
from collections import Counter

# artificially pause
# this is to simulate a real script
# which takes time
num_seconds_sleep = 0
time.sleep(num_seconds_sleep)

# print the "graph"
for line in sys.stdin.readlines():
    s = line.split()
    character = s[0]
    count = int(s[1])//2
    print(character, '#'*count)
