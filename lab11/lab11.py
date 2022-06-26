import re
from datetime import datetime

date_format = '%d/%b/%Y:%H:%M:%S'
date_start = datetime.strptime('01/Jul/1995:00:07:00', date_format)
date_end = datetime.strptime('01/Jul/1995:02:21:00', date_format)
file1 = open("access_log_Jul95", 'r')
lines = file1.readlines()
pattern = r'(\S+)\s+[-]+\s+[-]+\s+[\[](\S+)\s(\S+)]\s["](\S+)\s\D\w+\D(\w+)\S+\s\S+["]\s([200]\d+)\s\d+'
unique_set = set()
count = 0
for line in lines:
    x = re.match(pattern, line)
    if x:
        if date_start < datetime.strptime(x.groups()[1], '%d/%b/%Y:%H:%M:%S') < date_end:
            unique_set.add(x)
        elif datetime.strptime(x.groups()[1], '%d/%b/%Y:%H:%M:%S') > date_end:
            break
for i in unique_set:
    if i.group(5) == "NASA":
        print(f'{i.group(1)} {i.group(5)}')
print(len(unique_set))