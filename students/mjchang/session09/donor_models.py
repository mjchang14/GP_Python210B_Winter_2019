#!/usr/bin/env python

import math

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
        #create new database if one doesn't exist already
        if donors is None:
            self.donor_info = {}

        #iterate through donors with a dict
        else:
            self.donor_info = {x.name: x for x in donors}


    def donors(self):
        return self.donor_info.values()

    #create and return donor list as a string
    def donor_list(self):
        d_list = []
        for donor in self.donors:
            d_list.append(donor.name)
        return '\n'.join(d_list)


    def add_donor(self, name):
        donor = Donor(name)
        self.donor_info[donor] = donor
        return donor


    def locate_donor(self, name, donation):
        name = name.title()
        
        if name in donor_info:
            return name
        else:
            try:
                new_donor = self.donor_info[Donor.name]
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
        name = donor.name
        gifts = donor.donation
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = sum(gifts)/len(gifts)
        for name, gifts in self.donor_info.values():
            spreadsheet.append(name, total_gifts, num_gifts, avg_gift)

    #sort the report by total donation
        spreadsheet.sort(key = sort_key)
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