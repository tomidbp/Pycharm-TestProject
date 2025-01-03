
import sys

import pytest
pytestmark = pytest.mark.skipif(sys.platform != 'win32', reason="Will only only on win32")


const = 9/5
def cent_to_fah(cent=0):
    fah = (cent * const) + 32
    return fah

#print (cent_to_fah())
@pytest.mark.skip(reason="skipping for no reason")
def test_case01():
    assert type(const) == float

#@pytest.mark.skipif(sys.version_info > (3,6), reason="does not work py v above")
@pytest.mark.skipif(cent_to_fah()==32, reason="default value test, so skipping")
def test_case02():
    assert cent_to_fah() == 32

@pytest.mark.skipif(pytest.__version__ < '0.1.0', reason="pytest version 3.13.0")
def test_case03():
    assert cent_to_fah(38) == 100.4