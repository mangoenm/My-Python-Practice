"""
Script that allows you to create a contact book. Add, edit, and delete contacts
In addittion, you'll be able to view all your contacts and their details in one place.
Save contacts to a db and csv.
Must be configurable. Have a properties file that you can change and make the app save to a db or csv.
"""

# add contacts in lists (add name, add number)
# create pandas dataframe
# export dataframe to a csv file

import pandas as pd

def add_contacts():

    name_list = []
    contact_num_list = []
    num = int(input("How many contacts do you want to add: "))

    for i in range(num):
        name = input("Enter name: ")
        contact_num = input("Enter contact number: ")

        name_list.append(name)
        contact_num_list.append(contact_num)
        #print(name_list)
        #print(contact_num_list)

    contacts = {
            'Contact Name':name_list,
            'Contact number' :contact_num_list
    }
    df = pd.DataFrame(contacts)
    print("Create DataFrame:\n",df)

    df.to_csv('C:/Users/Naomi/Desktop/contacts.csv')

def delete_contacts():

    df = pd.read_csv("C:/Users/Naomi/Desktop/contacts.csv")
    df.head()
    print(df)

    #delete c
    df = df[df["Contact Name"].str.contains("Naomi") == False]
    print(df)
    
    #Save csv
    


#add_contacts()
delete_contacts()