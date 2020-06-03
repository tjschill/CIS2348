"""
Author: Schilling, Thomas, J
StudentID: 1937109
File: 5.19 ZyLab - CIS2348
"""

# Print Menu
print("Davy's auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12")
services = {"Oil change":35, "Tire rotation":19, "Car wash": 7, "Car wax": 12, "-":0}

# Prompt user for 2 services from menu
service1 = input("\nSelect first service:")
service2 = input("\nSelect second service:")

# Calculate total cost
total = services[service1] + services[service2]

# Output Invoice. Allowing for option No Service with input '-'
print("\n\nDavy's auto shop invoice")
if service1 != "-":
    print("\nService 1: {}, ${}".format(service1,services[service1]))
else:
    print("\nService 1: No service")
if service2 != "-":
    print("Service 2: {}, ${}".format(service2,services[service2]))
else:
    print("Service 2: No service")
print("\nTotal: ${}".format(total))