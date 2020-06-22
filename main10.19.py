"""
Author: Schilling, Thomas, J
StudentID: 1937109
File: 10.19 ZyLab - CIS2348
"""


# Type code for classes here

# Type code for classes here

class ItemToPurchase:

    def __init__(self, name="none", price=0, quantity=0, item_description="none"):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.item_description = "none"

    def print_item_cost(self):
        total = self.price * self.quantity
        print("{} {} @ ${} = ${}".format(self.name, self.quantity, self.price, total))
        return total

    def print_item_description(self):
        print("{}: {}.".format(self.name, self.item_description))


class ShoppingCart:

    def __init__(self, customer_name="none", current_date="January 1, 2016", cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self):
        print("\nADD ITEM TO CART")
        add_name = input("Enter the item name:\n")
        add_description = input("Enter the item description:\n")
        add_price = int(input("Enter the item price:\n"))
        add_quantity = int(input("Enter the item quantity:\n"))
        item = ItemToPurchase(add_name, add_price, add_quantity, add_description)
        self.cart_items.append(item)

    def remove_item(self):
        found = False
        print("\nREMOVE ITEM FROM CART")
        remove_name = input("Enter name of item to remove:\n")
        for item in self.cart_items:
            if item.name == "remove_name":
                found = True
                self.cart_items.remove(item)
        if found == False:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self):  # FINISH THIS ONE FIRST
        print("\nCHANGE ITEM QUANTITY")
        modify_name = input("Enter name of item name:\n")
        modify_quantity = input("Enter the new quantity:\n")
        for item in self.cart_items:
            if item.name == "modify_name":
                item.quantity = modify_quanitity

    def get_num_items_in_cart(self):
        num = 0
        for item in self.cart_items:
            num += item.quantity
        return num

    def get_cost_of_cart(self):
        cost = 0
        for item in self.cart_items:
            cost += (item.price * item.quantity)
        return cost

    def print_total(self):
        pass

    def print_descriptions(self):
        print("\nOUTPUT ITEMS' DESCRIPTIONS")
        print("{}'s Shopping Cart - {}\n".format(self.customer_name, self.current_date))
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()

    def output_shopping_cart(self):
        print("OUTPUT SHOPPING CART")
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        num = 0
        for item in self.cart_items:
            num += item.quantity
        print("Number of Items: {}\n".format(num))
        total = 0
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        for item in self.cart_items:
            total += item.print_item_cost()
        print("\nTotal: ${}".format(total))


menu = "\nMENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit"

if __name__ == "__main__":

    def print_menu(ShoppingCart):
        user_input = ''
        while user_input != 'q':
            print(menu)
            user_input = ''
            while user_input not in ['a', 'r', 'c', 'i', 'o', 'q']:
                user_input = input("\nChoose an option:")
            print()
            if user_input == 'a':
                ShoppingCart.add_item()
            elif user_input == 'r':
                ShoppingCart.remove_item()
            elif user_input == 'c':
                ShoppingCart.modify_item()
            elif user_input == 'i':
                ShoppingCart.print_descriptions()
            elif user_input == 'o':
                ShoppingCart.output_shopping_cart()
            elif user_input == 'q':
                break


    customer_name = input("Enter customer's name:\n")
    todays_date = input("Enter today's date:\n")

    print("\nCustomer name: {}".format(customer_name))
    print("Today's date: {}".format(todays_date))

    customer_cart = ShoppingCart(customer_name, todays_date)

    print_menu(customer_cart)

