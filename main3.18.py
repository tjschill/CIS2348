"""
Author: Schilling, Thomas, J
StudentID: 1937109
File: 3.18 ZyLab - CIS2348
"""

import math

# Dictionary of paint colors and cost per gallon
paint_colors = {
    'red': 35,
    'blue': 25,
    'green': 23
}

# Prompt user to input wall's height and width
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))

# Calculate and output wall area
wall_area = wall_height * wall_width
print('Wall area: {} square feet'.format(wall_area))

# Calculate and output the amount of paint in gallons needed to paint the wall

gallons = wall_area / 350
print("Paint needed: {:.2f} gallons".format(gallons))

# Calculate and output the number of 1 gallon cans needed to paint the wall, rounded up to nearest integer

cans = int(math.ceil(gallons))
print("Cans needed: {} can(s)\n".format(cans))

#  Calculate and output the total cost of paint can needed depending on color

color = input("Choose a color to paint the wall:\n")
cost = paint_colors[color] * cans
print("Cost of purchasing {} paint: ${}".format(color, cost))


