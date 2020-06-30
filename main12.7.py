"""
Author: Schilling, Thomas, J
StudentID: 1937109
File: 12.7 ZyLab - CIS2348
"""


def get_age():
    age = int(input())
    # TODO: Raise excpetion for invalid ages
    if age < 18 or age > 75:
        raise ValueError('Invalid age.')
    return age


# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * .7
    print("Fat burning heart rate for a {} year-old: {:.1f} bpm".format(age, heart_rate))
    return heart_rate


if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()

    #       and handle the exception
    try:
        age = get_age()
    except ValueError as excpt:
        print("Invalid age.\nCould not calculate heart rate info.\n")
    heart_rate = fat_burning_heart_rate(age)