#!/usr/bin/python

import sys
import csv

oldKey = None
count = 0
agg_answ_length = 0

reader = csv.reader(sys.stdin,delimiter='\t')
writer = csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_ALL)

for line in reader:
    if len(line) != 3:
        continue
    qstn_nd_id, qstn_length, answ_length = line
    qstn_length = int(qstn_length)
    answ_length = int(answ_length)
    thisKey = qstn_nd_id #node_id
    if oldKey and thisKey != oldKey:
        if agg_answ_length != 0:
            avg_answ_len = float(agg_answ_length)/count
        else:
            avg_answ_len = 0
        
        print "{0}\t{1}\t{2}".format(oldKey, old_qs_len, avg_answ_len)
        count = 0
        agg_answ_length = 0

    oldKey = thisKey
    if qstn_length == 0:
        agg_answ_length += answ_length
        count += 1
    else:
        old_qs_len = qstn_length

if oldKey != None:
    if agg_answ_length != 0:
        avg_answ_len = agg_answ_length/count
    else:
        avg_answ_len = 0
        print "{0}\t{1}\t{2}".format(oldKey, old_qs_len, avg_answ_len)
