#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin,delimiter='\t')
writer = csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_ALL)
oldKey = None
for line in reader:
    if line[1] == 'A':
        user_ptr_id,flag,reputation,gold,silver,bronze = line
        data = user_ptr_id.strip().split('_')
        author_id = data[0]
    else:
        author_id,flag,node_id,title,tagnames,node_type,parent_id,abs_parent_id,added_at,score = line
        data = author_id.strip().split('_')
        author_id = data[0]
        writer.writerow([author_id,node_id,title,tagnames,node_type,parent_id,abs_parent_id,added_at,score,reputation,gold,silver,bronze])
        
