"""
Author: Schilling, Thomas, J
StudentID: 1937109
File: 12.9 ZyLab - CIS2348
"""

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    # FIXME: The following line will throw ValueError exception
    #        Insert try/except blocks to catch the exception.
    try:
        int(parts[1])
    except ValueError as excpt:
        parts[1] = -1
    age = int(parts[1]) + 1
    print('{} {}'.format(name, age))

    # Get next line
    parts = input().split()
    name = parts[0]