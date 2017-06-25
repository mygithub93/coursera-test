#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin,delimiter='\t')
writer = csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_ALL)

oldKey = None
tlist = []

for line in reader:
    if len(line) != 2:
        continue
    thisKey, thisValue = line
    
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", tlist
        tlist = []

    oldKey = thisKey
    tlist.append(int(thisValue))

if oldKey != None:
    print oldKey, "\t", tlist
    tlist = []
    
