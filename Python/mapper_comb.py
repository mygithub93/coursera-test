#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin,delimiter='\t')
writer = csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_ALL)

for line in reader:
    if len(line) == 19 and line[0] != 'id':
        flag = 'B'
        node_id = line[0]
        title = line[1]
        tagnames = line[2]
        author_id = line[3]
        node_type = line[5]
        parent_id = line[6]
        abs_parent_id = line[7]
        added_at = line[8]
        score = line[9]
        author_id = author_id +'_'+flag
        writer.writerow([author_id,flag,node_id,title,tagnames,node_type,parent_id,abs_parent_id,added_at,score])
        
    elif len(line) == 5 and line[0] != 'user_ptr_id':
        flag = 'A'
        user_ptr_id,reputation,gold,silver,bronze = line
        user_ptr_id = user_ptr_id+'_'+flag
        writer.writerow([user_ptr_id,flag,reputation,gold,silver,bronze])


