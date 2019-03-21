#!/usr/bin/env python

import math
import sys
import os
import datetime

def get_donor_data():
    """
    reconfigured the donor database to return a list that uses classes
    instead of dictionaries to store and format the donor info
    """

    return [Donor("Eliza Sommers", [4000, 250, 70]),
            Donor("Tao Chien", [350, 1000, 225]), 
            Donor("Joaquin Andieta", [100, 25]), 
            Donor("Paulina Rodriguez", [50000]), 
            Donor("Jacob Todd", [75, 80]),
            ]



class Donor():
    """
    info on a single donor
    """
    def __init__(self, name, donation=None):
        self.name = name.title()
        if donation is None:
            self.donation = []
        else:
            try:
                self.donation = list(donation)
            except TypeError:
                self.donation[donation]

    @staticmethod
    def standard_name(name):
        """
        capitalizing name to give it a standard format for comparison
        """
        return name.title()


    @staticmethod
    def valid_donation(donation):
        donation = float(donation)
        if math.isnan(donation):
            raise ValueError("Enter a number")

        if donation < 0.01:
            raise ValueError("Donation must be at least $0.01")

        return donation
        

    def add_donation(self, amt):
        amt = self.valid_donation(amt)
        self.donation.append(amt)

    @property
    def recent_donation(self):
        try:
            return self.donation[-1]
        except IndexError:
            return None


    def gen_letter(self, donor):
        pass
    


    
class DonorCollection():
    """
    database of all donors - use encapsulation
    """
    def __init__(self, donors=None):
        #create new database if one doesn't exist already, use dicts?
        if donors is None:
            self.donor_info = {}

        #iterate through donors with a dict
        else:
            self.donor_info = {x.name: x for x in donors}


    @property
    def donors(self):
        return self.donor_info.values()


    def donor_list(self):
        """
        create and return donor list as a string
        that way it can be printed in list format with line returns
        """
        d_list = []
        for donor in self.donors:
            d_list.append(donor.name)
        return '\n'.join(d_list)


    def add_donor(self, name):
        donor = Donor(name)
        self.donor_info[donor] = donor
        return donor


    def locate_donor(self, name):
        """
        check for donor in the db, breaking this out from checking for 
        and creating a new donor
        """
        return self.donor_info.get(Donor.standard_name(name))
        
        
    def check_add_donor(self, name, donation):
        """
        check for a donor in db, if the inputted name isn't there
        create a new donor and add their donation
        """

        try:
            new_donor = self.donor_info[Donor.standard_name(name)]
        except KeyError:
            new_donor = self.add_donor(name)
        
        new_donor.add_donation(donation)
        return new_donor


    @staticmethod    
    def sort_key(data):
        return data[1]

    def donor_report(self):
        """
        create list of donor name, total given, number of gifts, average gift
        sort the list
        create the report
        """
     
        spreadsheet = []
        for donor in self.donor_info.values():
            name = donor.name
            gifts = donor.donation
            total_gifts = sum(gifts)
            num_gifts = len(gifts)
            avg_gift = sum(gifts)/len(gifts)
            spreadsheet.append((name, total_gifts, num_gifts, avg_gift))

        #sort the report by total donation
        spreadsheet.sort(key=self.sort_key)
        d_report = []
        d_report.append("{:<30} | {:<12} | {:>15} | {:12}".format("Donor Name",
                                                                  "Total Given", 
                                                                  "Number of Gifts", 
                                                                  "Average Gift"))


        d_report.append("-"*79) #print the dashed line
        for data in spreadsheet:    
            d_report.append("{:<30}  ${:12.2f}   {:>15}  ${:12.2f}".format(*data))
        return"\n".join(d_report)

    # @property
    # def total_donations(self):
    #     return sum(self.donation)

    # #no property needed for number of donations, use len(self.donation)

    # @property
    # def average_donation(self):
    #     return self.total_donations / len(self.donation)

    def write_letter(self, donor):
        """
        create a thank you letter to the donor
        """
        return ('Dear {},'
                '\n\nOn behalf of all of us,' 
                'we thank you for your generous donation of $   {:10.2f}. '
                '\n You have really helped the community!'.format(donor.name, donor.recent_donation))


    def write_to_disk(self):

        path = os.getcwd()
        folder = path + '/donor_letters/'
        os.mkdir(folder)
        os.chdir(folder)
        for donor in self.donor_info.values():
            letter = self.write_letter(donor)
        
        timestamp = str(datetime.date.today())
        filename = donor.name.replace(" ", "_") + timestamp + ".txt"
        open(filename, 'w').write(letter)
