#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin,delimiter='\t')
writer = csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_ALL)

for line in reader:
    if len(line) != 19 or line[0] == 'id':
        continue
    node_id = line[0]
    post_length = len(line[4])
    node_type = line[5].lower()  #question,answer,comment
    parent_id = line[6]
    abs_parent_id = line[7]
    if node_type == 'question':
        answ_length = 0
        writer.writerow([node_id,post_length,answ_length])
    elif node_type == 'answer':
        qstn_length = 0
        writer.writerow([abs_parent_id,qstn_length,post_length])
