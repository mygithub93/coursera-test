#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin,delimiter='\t')
writer = csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_ALL)

dict = {}
totCount = 0
oldTag = None

def MyFn(t):
    return t[1]

for line in reader:
    if len(line) != 2:
        continue
    tag_name,count = line
    if oldTag and oldTag != tag_name:
        if len(dict) > 10:
            minCount = min(dict.values())
            for k,v in dict.items():
                 if totCount > minCount and v == minCount:
                      dict.pop(k)
                      dict[oldTag] = totCount
        else:
            dict[oldTag] = totCount

        totCount = 0

    oldTag = tag_name
    totCount = totCount + 1

if oldTag != None:
    if len(dict) > 10:
        minCount = min(dict.values())
        for k,v in dict.items():
            if totCount > minCount and v == minCount:
                 dict.pop(k)
                 dict[oldTag] = totCount
    else:
        dict[oldTag] = totCount
for k,v in sorted(dict.items(),reverse=True,key=MyFn):
    writer.writerow([k,v])    
    
