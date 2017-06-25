#!/usr/bin/python

import sys

maxSale = 0.0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    
    if len(data) != 2:
        continue
    
    thisKey, thisValue = data
    val = float(thisValue)
    if oldKey and oldKey != thisKey.strip():
        print "{0}\t{1}".format(oldKey,maxSale)
        maxSale = 0.0
    
    oldKey = thisKey.strip()
    if val >= float(maxSale):
        maxSale = val

if oldKey != None:
    print "{0}\t{1}".format(oldKey,maxSale)
