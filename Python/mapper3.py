#!/usr/bin/python

import sys
import csv
import re


reader = csv.reader(sys.stdin,delimiter = '\t')

for line in reader:
    body = line[4].lower().strip()
    node_id = line[0].strip()
    text = re.split('[\s/\.,!\?:;"\(\)<>\[\]#\$=-]+',body)
    if 'fantastically' in text:
        print "{0}\t{1}".format('fantastically',node_id)

