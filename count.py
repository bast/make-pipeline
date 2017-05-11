#!/usr/bin/env python

"""
Counts the 10 most common characters
in a text.
"""

import sys
import time
from collections import Counter

# read string s from standard input
s = sys.stdin.read()

# artificially pause
# this is to simulate a real script
# which takes time
num_seconds_sleep = 0
time.sleep(num_seconds_sleep)

# throw away punctuation and spaces
# and convert to lowercase
s = [x.lower() for x in s if x.isalpha()]

# print result
for (character, count) in Counter(s).most_common(10):
    print(character, count)
