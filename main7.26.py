"""
Author: Schilling, Thomas, J
StudentID: 1937109
File: 7.25 ZyLab - CIS2348
"""


def exact_change(value):
    dollars = value // 100
    value -= dollars * 100
    quarters = value // 25
    value -= quarters * 25
    dimes = value // 10
    value -= dimes * 10
    nickels = value // 5
    value -= nickels * 5
    pennies = value
    return dollars, quarters, dimes, nickels, pennies


if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    if num_dollars > 1:
        print("{} dollarss".format(num_dollars))
    if num_dollars == 1:
        print("{} dollar".format(num_dollars))
    if num_quarters > 1:
        print("{} quarters".format(num_quarters))
    if num_quarters == 1:
        print("{} quarter".format(num_quarters))
    if num_dimes > 1:
        print("{} dimes".format(num_dimes))
    if num_dimes == 1:
        print("{} dime".format(num_dimes))
    if num_nickels > 1:
        print("{} nickels".format(num_nickels))
    if num_nickels == 1:
        print("{} nickel".format(num_nickels))
    if num_pennies > 1:
        print("{} pennies".format(num_pennies))
    if num_pennies == 1:
        print("{} penny".format(num_pennies))
    if input_val == 0:
        print("no change")