#!/usr/bin/env python

from donor_models import Donor, DonorCollection, get_donor_data
import math

db = DonorCollection(get_donor_data())

def menu():
    """
    collect the user menu input
    """
    response = int(input("""
        Please enter a number from the following options:
            1 - Send a Thank You to One Donor
            2 - Send a Thank You to All Donors
            3 - Create a Report
            4 - Quit
        """))
    return response


def thank_you_one():
    """
    collect the name, add it if it's new, record the new donation and 
    create a thank you message to the donor

    if the user inputs "list", show a list of existing donors in the database
    """
    #collect the name
    while True:
        name = input("Please enter a name (or 'list' for all donors): ")
        if name.lower() == "list":
            print(db.donor_list)
        else:
            break

    donor = db.locate_donor(name)
    
    while True:
        donation = int(input("Enter the donation amount: "))
        try:
            donation = Donor.valid_donation(entered_donation)
        except ValueError:
            print("Donation amount must be a number")

    donor.add_donation(amount)
    print(gen_letter(donor))


def thank_you_all():
    """
    save letters to all donors to disk
    """
    pass


def donor_report():
    """
    generate a donor report with donor name, total given, number of gifts,
    and average gift
    """
    print(db.donor_report())



def quit_program():
    SystemExit

def main():
    selection = {1: thank_you_one, 
                 2: thank_you_all, 
                 3: donor_report,
                 4: quit_program}
    while True:
        select = menu()
        try:
            selection[select]()
        except KeyError:
            print("Please select from the available options")