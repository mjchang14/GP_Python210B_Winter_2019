
import pytest
import os
from donor_models import Donor, DonorCollection, get_donor_data



db = get_donor_data()

def test_new_donor():
    """
    test that new donor is added, donation should be None. Test for 
    new donation in next test
    """
    donor = Donor("Mama Fresia")
    assert donor.name == "Mama Fresia"
    assert donor.recent_donation is None


def test_valid_donation():
    """
    add donation, check that it's a positive number
    check that it's a number
    validate that the amount is correct in db
    """
    #adding new donor - is there a simple way to get an existing donor???
    donor = Donor("Mama Fresia")

    with pytest.raises(ValueError):
        donor.valid_donation("-50")

    with pytest.raises(ValueError):
        Donor.valid_donation("not a number")

    

def test_add_donation():
    """
    adding a donation to an existing donor for the test
    """
    donor = Donor("Jacob Todd")
    donor.add_donation(500)
    assert donor.recent_donation == 500


def test_donor_list():
    """ create new donor list
    check random names and list length for errors
    """
    donor_db = DonorCollection(get_donor_data())
    new_list = donor_db.donor_list()

    assert "Eliza Sommers" in new_list
    assert "Tao Chien" in new_list
    assert len(new_list.split('\n')) == 5



def test_locate_donor():
    """
    check that donor exists - 1 assert for known donor with different 
    capitalization, 1 for donor not in db
    """
    new_donor = "Isabel Allende"
    assert new_donor not in db

    exist_donor = locate_donor("jacob todd")
    assert donor.name == "Jacob Todd"


def test_letter_gen():
    """
    test contents of letter
    """
    pass

def test_letters_to_disk():
    """
    check that the letters show up in the correct folder
    is there anything else that should/could be tested here?
    """
    pass


def test_donor_report():
    """
    test random lines in report, ex. header and one donor line
    """
    donor_db = DonorCollection(get_donor_data())
    d_report = donor_db.donor_report
    # print(d_report)
    assert d_report.startswith('Donor Name                     | Total Given  | Number of Gifts | Average Gift')
    assert "Paulina Rodriguez               $    50000.00                 1  $    50000.00" in d_report



