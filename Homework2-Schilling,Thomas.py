"""
Author: Schilling, Thomas, J
StudentID: 1937109
File: Homework2 - CIS2348
"""

month_dict = {'January':'1', 'February':'2', 'March':'3', 'April':'4', 'May':'5', 'June':'6', 'July':'7', 'August':'8', 'September':'9', 'October':'10', 'November':'11', 'December':'12'}

def date_format_checker(input_date):
    list = input_date.split()
    check = True
    if '  ' in input_date or '   ' in input_date:
        check = False
        return check
    if len(list) != 3:
        check = False
        return check
    if "," not in input_date:
        check = False
        return check
    if list[0] not in month_dict.keys():
        check = False
        return check
    if len(list[1]) < 2 or len(list[1]) > 3:
        check = False
        return check
    if len(list[1]) == 3:
        if list[1][:2].isnumeric() == False:
            check = False
            return check
        if int(list[1][0:2]) > 31:
            check = False
            return check
    if len(list[1]) == 2:
        if list[1][:1].isnumeric() == False:
            check = False
            return check
    if list[1][-1] != ',':
        check = False
        return check
    if list[2].isnumeric() == False:
        check = False
        return check
    return check

def reformat_date(input_date):
    list = input_date.split()
    month = month_dict[list[0]]
    day = list[1][0:-1]
    year = list[2]
    return "{}/{}/{}\n".format(month, day, year)


input_file = open('inputDates.txt', 'r')
input_file_lines = input_file.readlines()
input_file.close()

output_file = open('parsedDates.txt', 'w')


for input_date in input_file_lines:
    if input_date == '-1':
        break
    correct = date_format_checker(input_date)
    if correct == True:
        output_file.write(reformat_date(input_date))

output_file.close()

