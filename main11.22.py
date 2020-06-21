"""
Author: Schilling, Thomas, J
StudentID: 1937109
File: 11.22 ZyLab - CIS2348
"""

user_input = input()

list = user_input.split()

dict = {}

for word in list:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

for word in list:
    print(word, dict[word])