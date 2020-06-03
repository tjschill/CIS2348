"""
Author: Schilling, Thomas, J
StudentID: 1937109
File: Homework1 - CIS2348
"""

# Checks for correct formatting of input
def date_format_checker(input_date):
    month, day, year = 0,0,0
    if len(input_date) > 8:
        print("Error: Input too long")
        date_format = 'Incorrect'
        return date_format, month, day, year
    if len(input_date) < 8:
        print("Error: Input too short")
        date_format = 'Incorrect'
        return date_format, month, day, year
    month, day, year = date_processor(input_date)
    if month > 12 or day > 31:
        print("Error: Incorrect Date")
        date_format = 'Incorrect'
        return date_format, month, day, year
    else:
        date_format = 'correct'
        return date_format, month, day, year

# Processes input into 3 parts of date
def date_processor(input_date):
    input_date = int(input_date)
    month = input_date // 1000000
    day = (input_date % 1000000) // 10000
    year = input_date % 10000
    return month, day, year

# calculates age in years
def age_calculator(current_month, current_day, current_year, birthday_month, birthday_day, birthday_year):
    if current_month > birthday_month:
        return current_year - birthday_year
    elif current_month == birthday_month and current_day >= birthday_day:
        return current_year - birthday_year
    else:
        return current_year - birthday_year - 1

# Checks for birthday, gets age, and outputs message
def birthday_output(current_month, current_day, current_year, birthday_month, birthday_day, birthday_year):
    birthday = False
    if current_month == birthday_month and current_day == birthday_day:
        birthday = True
    age_years = age_calculator(current_month, current_day, current_year, birthday_month, birthday_day, birthday_year)
    print("\nBirthday Calculator")
    print("Current Day")
    print("Month: {}".format(current_month))
    print("Day: {}".format(current_day))
    print("Year: {}".format(current_year))
    print("Birthday")
    print("Month: {}".format(birthday_month))
    print("Day: {}".format(birthday_day))
    print("Year: {}".format(birthday_year))
    print("You are {} years old.".format(age_years))
    if birthday == True:
        print("Happy Birthday!")






# Get the current date and the user's birthday
# Checks for incorrect formatting
# Process input into 3 parts of date
date_format = ''
while date_format != 'correct':
    input_date = input("Enter the current date in the format 'mmddyyyy'\n")
    date_format, current_month, current_day, current_year = date_format_checker(input_date)

date_format = ''
while date_format != 'correct':
    input_birthday = input("Enter your birthday in the format 'mmddyyyy'\n")
    date_format, birthday_month, birthday_day, birthday_year = date_format_checker(input_birthday)

# Check for Birthday and Output
birthday_output(current_month, current_day, current_year, birthday_month, birthday_day, birthday_year)


exit = input("\nPress 'enter' to exit")

