#!/usr/bin/python

import sys
import csv

oldKey = None
oldSid = None
count = 0
tdict = {}

reader = csv.reader(sys.stdin,delimiter='\t')
writer = csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_ALL)

for line in reader:
    if len(line) != 2:
        continue
    thisKey, thisHour = line
    thisSid,hr = thisKey.split("_")

    if oldKey and thisKey != oldKey:
        tdict[oldKey] = count
        count = 0
    
    oldKey = thisKey
    count += 1

    if oldSid and thisSid != oldSid:
        max_count = max(tdict.values())
        for k, v in tdict.items():
            if v >= max_count:
                a,b = k.split("_")
                writer.writerow([a,b])
        tdict={}

    oldSid = thisSid

if oldKey != None:
    max_count = max(tdict.values())
    for k,v in tdict.items():
        if v >= max_count:
            a,b = k.split("_")
            writer.writerow([a,b])
    
