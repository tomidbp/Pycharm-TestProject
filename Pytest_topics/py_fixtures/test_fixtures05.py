import pytest

@pytest.fixture(params=[(3,4), [3,5]], ids=['tuple', 'list'])
def fixture01(request):
    return request.param

@pytest.fixture(params=["access", "slice", "assign", "len"])
def fixtures02(request):
    return request.param

def test_fix_param01(fixture01):
    assert (type(fixture01)) in [tuple]

def test_fix_param02(fixture01, fixtures02):
    if (fixtures02 == "access"):
        assert (fixture01[0])
    elif (fixtures02 == 'slice'):
        assert fixture01[::-1]
    elif (fixtures02 == 'assign'):
        fixture01[0] = 99
        assert True
    elif (fixtures02 == 'len'):
        assert len(fixture01)