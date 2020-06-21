"""
Author: Schilling, Thomas, J
StudentID: 1937109
File: 11.27 ZyLab - CIS2348
"""


def add_player():
    new_jersey = int(input("\nEnter a new player's jersey number:\n"))
    new_rating = int(input("Enter the player's rating:\n"))
    dict[new_jersey] = new_rating


def remove_player():
    remove_jersey = int(input("\nEnter a jersey number:\n"))
    del dict[remove_jersey]


def update_player_rating():
    update_jersey = int(input("\nEnter a jersey number:\n"))
    update_rating = int(input("Enter a new rating for player:\n"))
    dict[update_jersey] = update_rating


def output_players_above_a_rating():
    rating_above = int(input("\nEnter a rating:\n"))
    print("\nABOVE {}".format(rating_above))
    list = []
    for key in dict.keys():
        list.append((key))
    list.sort()
    for key in list:
        if dict[key] > rating_above:
            print("Jersey number: {}, Rating: {}".format(key, dict[key]))


def output_roster():
    list = []
    for key in dict.keys():
        list.append((key))
    list.sort()
    print("\nROSTER")
    for key in list:
        print("Jersey number: {}, Rating: {}".format(key, dict[key]))


dict = {}

p1_jersey = int(input("Enter player 1's jersey number:\n"))
p1_rating = int(input("Enter player 1's rating:\n"))
p2_jersey = int(input("\nEnter player 2's jersey number:\n"))
p2_rating = int(input("Enter player 2's rating:\n"))
p3_jersey = int(input("\nEnter player 3's jersey number:\n"))
p3_rating = int(input("Enter player 3's rating:\n"))
p4_jersey = int(input("\nEnter player 4's jersey number:\n"))
p4_rating = int(input("Enter player 4's rating:\n"))
p5_jersey = int(input("\nEnter player 5's jersey number:\n"))
p5_rating = int(input("Enter player 5's rating:\n"))

dict[p1_jersey] = p1_rating
dict[p2_jersey] = p2_rating
dict[p3_jersey] = p3_rating
dict[p4_jersey] = p4_rating
dict[p5_jersey] = p5_rating

output_roster()

menu = "\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit"
user_input = ''
while user_input != 'q':
    print(menu)
    user_input = input("\nChoose an option:\n")
    if user_input == 'a':

        add_player()
    elif user_input == 'd':
        remove_player()
    elif user_input == 'u':
        update_player_rating()
    elif user_input == 'r':
        output_players_above_a_rating()
    elif user_input == 'o':  # Works
        output_roster()
    else:
        pass