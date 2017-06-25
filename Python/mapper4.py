#!/usr/bin/python

import sys
import csv
import re


reader = csv.reader(sys.stdin,delimiter = '\t')

for line in reader:
    body = line[4].lower().strip()
    text = re.split('[\s/\.,!\?:;"\(\)<>\[\]#\$=-]+',body)
    for word in text:
        print word

