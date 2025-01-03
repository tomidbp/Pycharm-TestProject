from pytest_bdd import scenario, scenarios, given, when, then
from pathlib import Path
import pytest

from Pytest_topics.bddpytest.test_bdd101 import featureFile, FEATURE_FILE
from Pytest_topics.utils.util import BASE_DIR

featureFileDir = 'myfeatures'
featureFile = 'fixtures.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

@pytest.fixture()
def setup_set():
    print("\n In fixture... setup() function... \n ")
    countries = {'Poland', 'America', 'Japan', 'Cambodia', 'Alaska'}
    return countries

@given('A datatype set')
def check_set_type(setup_set):
    print("In Background checking set type")
    if not isinstance(setup_set, set):
        pytest.xfail("The type is not set")

@given('The set is not empty')
def check_set_notempty(setup_set):
    if len(setup_set) == 0:
        pytest.xfail("In Background checking non-empty set")
    elif len(setup_set) > 3:
        while len(setup_set) > 3:
            setup_set.pop()
    return  setup_set


@given('A set with 3 elements', target_fixture='setup_set1')
def set_of_elems(setup_set):
    if len(setup_set) == 0:
        pytest.xfail("The set of elements is empty")
    elif len(setup_set) > 3:
        while len(setup_set) > 3:
            setup_set.pop()
    return setup_set

@when('Add 2 elements to the set')
def add_elements(setup_set1):
    setup_set1.add('India')
    setup_set1.add('Argentina')

@then('The set should have 5 elements')
def final_set_elements(setup_set1):
    print(setup_set1)
    assert len(setup_set1) == 5