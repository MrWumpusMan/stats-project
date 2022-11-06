import numbers
import os
import json
import gzip
import random
import pandas as pd
from urllib.request import urlopen

### load the meta data

data = []
with gzip.open('Electronics_5.json.gz') as f:
    count = 0
    for l in f:
        if count == 100:
            data.append(json.loads(l.strip()))
            count = 0
        else:
            count += 1
# total length of list, this number equals total number of products
print(len(data))

# print random items in the list

numbersalready = []
for i in range(1000):
    numFound = False
    while not numFound:
        num = random.randrange(len(data))
        if not (num in numbersalready):
            numFound = True
    print(num)
    print(data[num]["asin"])
    numbersalready.append(num)