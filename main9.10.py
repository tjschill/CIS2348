"""
Author: Schilling, Thomas, J
StudentID: 1937109
File: 9.10 ZyLab - CIS2348
"""

import csv

# Type your code here.

dict = {}

with open(input(), 'r') as csvfile:
    file = csv.reader(csvfile, delimiter=',')
    for line in file:
        for word in line:
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] += 1

for word in dict.keys():
    print(word, dict[word])
