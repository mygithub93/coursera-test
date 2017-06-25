#!/usr/bin/python

import sys

count = 0
for line in sys.stdin:
    text = line.strip()
    if text == 'fantastic':
        count += 1

print count

