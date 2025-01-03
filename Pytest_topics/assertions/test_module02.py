from sys import exc_info

import pytest


def testcase01():
    with pytest.raises(ZeroDivisionError):
        #assert (1/0)
        assert 3 > 3

def func1():
    raise ValueError("Exception func1 raised")

def test_case02():
    with pytest.raises(Exception) as excinfo:
        #assert (1,2,3) == (1,2,4)
        func1()
    print(str(excinfo))
    assert (str(excinfo.value)) == 'Exception fun1 raised'
    #this will be failed