from wsgiref.validate import assert_

import pytest

pytestmark = [pytest.mark.smoke, pytest.mark.strtest]

@pytest.mark.sanity
def test_str01():
    num = 9/4
    s1 = 'I like ' + 'pytest automation'
    assert str(num) == '2.25'
    assert s1 == 'I like pytest automation'
    assert s1 + str(num) == 'I like pytest automation2.25'

@pytest.mark.sanity
def test_str02():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert len(letters) == 26

def test_str03():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[0] == 'a'
    assert letters[-1] == 'z' == letters[25]

    #We start from 0 if we want to choose the first letter and -1 if we want to start with the last

@pytest.mark.sanity
@pytest.mark.str
def test_strslice():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert  letters[:] == letters #This will provide with the whole string
    assert letters[10:] == 'klmnopqrstuvwxyz' #This will start from the 10th alphabet and will go until the finish
    assert letters[-3:] == 'xyz' # This willl start from -3 meaning the last 3 alphabets, and will stop at the 3rd from the back
    assert letters[:21:5] == 'afkpu' #starts from the first 0 "a" after the 5th will be "f" and will continue to take every 5th alphabet till the 21st.

@pytest.mark.str
def test_strsplit():
    s1 = 'Python,Pytest and Automation'
    assert s1.split() == ['Python,Pytest', 'and', 'Automation'] #With no arguments in the bracket will split the whole string word my word.
    assert s1.split(',') == ['Python', 'Pytest and Automation']

# task TBD
#def test_strjoin():
#    pass
#    s1 = 'Python, Pytest and Automation'
#    l1 = ['Python, Pytest', 'and', 'Automation']
#    l2 = ['Python', 'Pytest and Automation']
#    assert ' '.join(l1) == s1