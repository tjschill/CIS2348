"""
Author: Schilling, Thomas, J
StudentID: 1937109
File: 10.17 ZyLab - CIS2348
"""


# Type code for classes here

class ItemToPurchase:

    def __init__(self, name="none", price=0, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def print_item_cost(self):
        total = self.price * self.quantity
        print("{} {} @ ${} = ${}".format(self.name, self.quantity, self.price, total))
        return total


if __name__ == "__main__":
    # Type main section of code here

    print("Item 1")
    name1 = input("Enter the item name:\n")
    price1 = int(input("Enter the item price:\n"))
    quantity1 = int(input("Enter the item quantity:\n"))

    item1 = ItemToPurchase(name1, price1, quantity1)

    print("\nItem 2")
    name2 = input("Enter the item name:\n")
    price2 = int(input("Enter the item price:\n"))
    quantity2 = int(input("Enter the item quantity:\n"))

    item2 = ItemToPurchase(name2, price2, quantity2)

    print("\nTOTAL COST")
    total1 = item1.print_item_cost()
    total2 = item2.print_item_cost()
    print("\nTotal: ${}".format(total1 + total2))
