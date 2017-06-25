#!/usr/bin/python

import sys

oldKey = None
inv_idx = None

for line in sys.stdin:

    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    thisKey,node_id = data

    if oldKey and oldKey != thisKey:
        
        print oldKey,"\t",inv_idx.strip(',')
        inv_idx = None
    
    if inv_idx is None:
        inv_idx = node_id + ','
    else:
        inv_idx += node_id + ','

    oldKey = thisKey
    

if oldKey != None:
    print oldKey,"\t",inv_idx.strip(',')
