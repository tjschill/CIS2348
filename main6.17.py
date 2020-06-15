"""
Author: Schilling, Thomas, J
StudentID: 1937109
File: 6.17 ZyLab - CIS2348
"""

word = input()
password = ''
dict = {'i':'!', 'a':'@', 'm':'M', 'B':'8', 'o':'.'}

for char in word:
    if char in dict:
        password += dict[char]
    else:
        password += char
print(password + "q*s")