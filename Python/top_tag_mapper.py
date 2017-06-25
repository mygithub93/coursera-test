#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin,delimiter='\t')
writer = csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_ALL)

for line in reader:
    if len(line) != 19 or line[0] == 'id':
        continue
    tag_name = line[2].strip().split(" ")
    node_type = line[5].strip().lower()
    for tag in tag_name:
        writer.writerow([tag, 1])
