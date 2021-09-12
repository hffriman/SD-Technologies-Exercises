from unittest import mock
from new_postinumerot import *

# WRITTEN AND COMMENTED BY HENRY FRIMAN 2021

# TEST 1:
# THIS TEST WRITES STRING "Askola" IN THE
# INPUT SECTION OF THE FUNCTION find_postnumbers
# --> THE FUNCTION CREATES A LIST WHICH CONTAINS
#     ALL POST NUMBERS THAT ARE KEYS  TO VALUE "ASKOLA"
# --> TEST: IF THE LENGTH OF THE LIST IS 8, THE TEST IS PASSED

def test_find_postnumbers_1():
    with mock.patch('builtins.input', return_value="Askola"):
    	assert len(find_postnumbers()) == 8


# TEST 2:
# THIS TESTS WORKS THE SAME WAY AS THE FIRST ONE,
# BUT INSTEAD OF 'Askola' IT PUTS 'Tähtelä' TO INPUT
# ----> IF THERE IS ONLY ONE KEY IN THE LIST THAT
#       HAS THE VALUE 'TÄHTELÄ', THE TEST IS PASSED
def test_find_postnumbers_2():
    with mock.patch('builtins.input', return_value="Tähtelä"):
        assert len(find_postnumbers()) == 1 
