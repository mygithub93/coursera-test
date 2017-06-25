#!/usr/bin/python

import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin,delimiter='\t')
writer = csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_ALL)

for line in reader:
    if len(line) != 19 or line[0] == 'id':
        continue
    std_id = line[3]
    added_at = line[8].strip()
    t = added_at[:19]
    hr = datetime.strptime(t,'%Y-%m-%d %H:%M:%S').hour
    key = std_id+'_'+str(hr)
    writer.writerow([key,hr])
