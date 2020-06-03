"""
Author: Schilling, Thomas, J
StudentID: 1937109
File: 2.19 ZyLab - CIS2348
"""

# Input Variables

lemon_juice = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input("Enter amount of water (in cups):\n"))
agave = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n"))

# Output Variables

print("\nLemonade ingredients - yields {:.2f} servings".format(servings))
print("{:.2f} cup(s) lemon juice".format(lemon_juice))
print("{:.2f} cup(s) water".format(water))
print("{:.2f} cup(s) agave nectar".format(agave))

# Input desired servings

num = float(input("\nHow many servings would you like to make?\n"))

# Output converted to desired servings

print("\nLemonade ingredients - yields {:.2f} servings".format(num))
print("{:.2f} cup(s) lemon juice".format((lemon_juice / servings) * num))
print("{:.2f} cup(s) water".format((water / servings) * num))
print("{:.2f} cup(s) agave nectar".format((agave / servings) * num))

# Output converted to gallons

print("\nLemonade ingredients - yields {:.2f} servings".format(num))
print("{:.2f} gallon(s) lemon juice".format(((lemon_juice / servings) * num) / 16))
print("{:.2f} gallon(s) water".format(((water / servings) * num) / 16))
print("{:.2f} gallon(s) agave nectar".format(((agave / servings) * num) / 16))
