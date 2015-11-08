import csv
import numpy as np

data = []

with open('cleaned.csv', 'rb') as csvfile:
    for line in csvfile:
        data.append([x.strip() for x in line.split(',')])
        #', '.join(row)\
data = np.asarray(data)
for row in data:
    print row


