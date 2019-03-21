
import pytest
import os
import cli_main
from donor_models import Donor, DonorCollection, get_donor_data



db = DonorCollection(get_donor_data())

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
    exist_donor = db.locate_donor("jacob todd")
    assert exist_donor.name == "Jacob Todd"

    new_donor = "Isabel Allende"
    assert new_donor is None


def test_check_add_donor():
    """
    add a donation for a donor and check that it is added correctly
    check that name is in db
    check most recent donation
    """
    donor = db.check_add_donor("Tao Chien", 300)

    assert donor.name == "Tao Chien"
    assert donor.recent_donation == 300



def test_write_letter():
    """
    test contents of letter
    """
    donor = Donor("Haruki Murakami", [1000, 1500])
    note = db.write_letter(donor)
    assert note.startswith("Dear Haruki Murakami,")
    expected = ('On behalf of all of us,' 
                'we thank you for your generous donation of $      1500.00. '
                '\n You have really helped the community!')
    assert expected in note

def test_write_to_disk():
    """
    check that the letters show up in the correct folder
    is there anything else that should/could be tested here?
    """
    db.write_to_disk()

    assert os.path.isfile('Tao Chien_'+timestamp+'.txt')
    assert os.path.isfile('Joaquin Andieta_'+timestamp+'.txt')
    with open('Tao Chien_'+timestamp+'.txt') as f:
        char_count = len(f.read())


def test_donor_report():
    """
    call report
    test random lines in report, ex. header and one donor line
    """
    donor_db = DonorCollection(get_donor_data())
    d_report = donor_db.donor_report()
    # print(d_report)
    assert d_report.startswith('Donor Name                     | Total Given  | Number of Gifts | Average Gift')
    assert "Paulina Rodriguez               $    50000.00                 1  $    50000.00" in d_report



