#!/usr/bin/python

import sys

totSale = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    thisKey, thisValue = data

    if oldKey and oldKey != thisKey:
        print oldKey.strip(), "\t", totSale
        oldKey = thisKey
        totSale = 0
    
    oldKey = thisKey
    totSale += float(thisValue)

if oldKey != None:
    print oldKey.strip(), "\t", totSale
