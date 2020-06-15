"""
Author: Schilling, Thomas, J
StudentID: 1937109
File: 8.10 ZyLab - CIS2348
"""

string = input()

newstring = string.replace(" ", "")
reverse = newstring[::-1]
if newstring == reverse:
    print("{} is a palindrome".format(string))
else:
    print("{} is not a palindrome".format(string))