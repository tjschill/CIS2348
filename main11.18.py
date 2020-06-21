"""
Author: Schilling, Thomas, J
StudentID: 1937109
File: 11.18 ZyLab - CIS2348
"""

user_input = input()
list = user_input.split()

list2 = []
for num in list:
    num = int(num)
    if num >= 0:
        list2.append(num)

list2.sort()

for num in list2:
    print(num, end=' ')