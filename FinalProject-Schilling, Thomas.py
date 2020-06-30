"""
Author: Schilling, Thomas, J
StudentID: 1937109
File: Final Project - CIS2348
"""

import csv
import datetime

def csv_to_list(input_file):
    output_list = []
    with open(input_file, 'r') as csvfile:
        CSV_list = csv.reader(csvfile, delimiter=',')
        row_num = 1
        for row in CSV_list:
            output_list.append(row)
            row_num += 1
    return output_list

def list_to_csv(filename, list):
    with open(filename, 'w+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for line in list:
            writer.writerow(line)


##### PART 1

### OPEN THREE INPUT FILES INTO 3 LISTS

Manufacturer_List = csv_to_list('FinalProjectManufacturerList.csv')
Price_List = csv_to_list('FinalProjectPriceList.csv')
Service_Dates_List = csv_to_list('FinalProjectServiceDatesList.csv')

### 1a TAKE 3 LISTS INTO FULL LIST WITH ALL INFORMATION

Full_Inventory = Manufacturer_List
for full_line in Full_Inventory:
    for price_line in Price_List:           # ADD PRICE
        if full_line[0] == price_line[0]:
            full_line.append(price_line[1])
    for date_line in Service_Dates_List:    # ADD SERVICE DATE
        if full_line[0] == date_line[0]:
            full_line.append(date_line[1])
    full_line.append(full_line[3])          # COPY DAMAGED TO END
    full_line.pop(3)                        # REMOVE OLD DAMAGED

Full_Inventory.sort()                       # SORT BY ID
Full_Inventory.sort(key=lambda x: x[1])     # SORT BY MANUFACTURER ALPHABETICALLY


### 1b MAKE LIST FOR TYPES, SUBLIST FOR EACH TYPE

Type_List = []
for line in Full_Inventory:         # CREATE LIST WITH SUBLIST FOR EACH TYPE
    if [line[2]] in Type_List:
        pass
    else:
        Type_List.append([line[2]])
for full_line in Full_Inventory:         # ADD ITEMS TO CORRECT SUBLIST
    for line in Type_List:
        if full_line[2] == line[0]:
            line.append([full_line[0], full_line[1], full_line[3], full_line[4], full_line[5]])


### 1c MAKE LIST FOR ITEMS WITH PAST SERVICE DATE
Past_Service_Date_List = []

date_today = datetime.date.today()      # GET TODAYS DATE

for line in Full_Inventory:             # MAKE SERVICE DATES INTO datetime.date CLASSES
    date_list = line[4].split("/")
    service_date = datetime.date(int(date_list[2]), int(date_list[0]), int(date_list[1]))
    if service_date < date_today:
        Past_Service_Date_List.append(line)
Past_Service_Date_List.sort(key=lambda x: x[4]) # SORT BY DATE


### 1d MAKE LIST FOR DAMAGED ITEMS
Damaged_Inventory_List = []

for full_line in Full_Inventory:
    if full_line[5] == 'damaged':
        Damaged_Inventory_List.append([full_line[0], full_line[1], full_line[2], full_line[3], full_line[4]])
Damaged_Inventory_List.sort(key=lambda x: x[3])  # SORT BY PRICE


### OUTPUT CSV FILES

#1a
list_to_csv('FullInventory.csv', Full_Inventory)
#1b
for type_line in Type_List:
    list_to_csv('{}Inventory.csv'.format(type_line[0].capitalize()), type_line[1:])
#1c
list_to_csv('PastServiceDateInventory.csv', Past_Service_Date_List)
#1d
list_to_csv('DamagedInventory.csv', Damaged_Inventory_List)





##### PART 2

### QUERY USER TO CHECK FOR ITEM IN INVENTORY

user_query = ' '
while user_query != 'q':
    print("\nTo check for an item in inventory,")
    print("type the manufacturer and item in the format")
    print("'Manufacturer Item' and press enter. ('q' to quit)")
    user_query = input()
    print()
    user_query_list = user_query.split()
    manufacturer = ''
    item_type = ''
    Item_List = []          # List in case there are multiple items
    Found = False


### SEARCH FOR ITEM IN INVENTORY
    for word in user_query_list:
        for line in Full_Inventory:
            if word == line[1] or word.capitalize() == line[1] or word.lower() == line[1] or word + ' ' == line[1] or word.lower() + ' ' == line[1] or word.capitalize() + ' ' == line[1]:
                manufacturer = line[1]
    if manufacturer != '':
        for word in user_query_list:
            for line in Full_Inventory:
                if line[1] == manufacturer:
                    if word == line[2] or word.capitalize() == line[2] or word.lower() == line[2]:
                        date_list = line[4].split("/")                          # CHECK SERVICE DATE
                        service_date = datetime.date(int(date_list[2]), int(date_list[0]), int(date_list[1]))
                        if service_date >= date_today and line[5] != 'damaged':   # CHECK DAMAGED
                            item_type = line[2]
                            Found = True
                            Item_List.append(line)

### OUTPUT FOUND ITEM
    if Found == True:
        Item_List.sort(key=lambda x: x[3])     # SORT LIST BY PRICE
        Item_Price = Item_List[0][3]
        print("Your item is: {} {} {} {}".format(Item_List[0][0], Item_List[0][1], Item_List[0][2], Item_List[0][3]))   # OUTPUT ITEM


### FIND SIMILAR ITEM TO CONSIDER
        Similar_Item_List = []
        for line in Full_Inventory:
            if line[1] != manufacturer and line[2] == item_type:
                date_list = line[4].split("/")                          # CHECK SERVICE DATE
                service_date = datetime.date(int(date_list[2]), int(date_list[0]), int(date_list[1]))
                if service_date >= date_today and line[5] != 'damaged':  # CHECK DAMAGED
                    Similar_Item_List.append(line)
        Similar_Item_List.sort(key=lambda x: x[3])  # SORT LIST BY PRICE
        if len(Similar_Item_List) > 0:
            for item in Similar_Item_List:
                Similar_Item = Similar_Item_List[min(range(len(Similar_Item_List)), key=lambda i: int(Similar_Item_List[i][3]) - int(Item_Price))]  # FIND SIMILAR ITEM WITH CLOSEST PRICE

            print("\nYou may, also, consider: {} {} {} {}".format(Similar_Item[0], Similar_Item[1], Similar_Item[2], Similar_Item[3])) # OUTPUT SIMILAR ITEM


    else:
        print("No such item in inventory (Check Spelling)")
