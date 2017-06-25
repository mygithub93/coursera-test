#!/usr/bin/python

import sys

totSales = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    thisKey, thisValue = data

    if oldKey and oldKey != thisKey:
        print "{0}\t{1}".format(oldKey,totSales)
        totSales = 0

    oldKey = thisKey
    totSales += float(thisValue)

if oldKey != None:
    print "{0}\t{1}".format(oldKey,totSales)
