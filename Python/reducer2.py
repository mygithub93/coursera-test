#!/usr/bin/python

import sys

counter = 0
oldKey = None
maxpath = None
maxcount = 0

for line in sys.stdin:
    path = line.strip()
    if len(path) <= 1:
        continue
    if oldKey and oldKey != path:
        if counter > maxcount:
            maxcount = counter
            maxpath = oldKey
        counter = 0

    oldKey = path
    counter += 1

if oldKey != None:
    print maxpath,"\t",maxcount
