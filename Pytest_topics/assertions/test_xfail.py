import sys

import pytest

def test_strjoin():
    s1 = 'Python, Pytest and Automation'
    l1 = ['Python, Pytest', 'and', 'Automation']
    l2 = ['Python', ' Pytest and Automation']
    assert ' '.join(l1) == s1

    joined_string = ' '.join(l1)
    print(f"Joined string: {joined_string}") #f is optional to add so that will add a text


@pytest.mark.xfail
def test_str04(reason="unknown issues"):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[100]

@pytest.mark.xfail(sys.platform=='win32', reason="works only on windows w32")
def test_str05():
    letters = 'abcd'
    num = 1234
    assert letters + num == 'abcs1234'
