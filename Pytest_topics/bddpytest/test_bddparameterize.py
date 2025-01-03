from turtledemo.penrose import start

from pytest_bdd import scenario, scenarios, given, when, then, parsers
from pathlib import Path
import pytest

from Pytest_topics.bddpytest.test_bdd101 import featureFileDir
from Pytest_topics.bddpytest.test_bddfixtures import featureFile
from Pytest_topics.utils.util import BASE_DIR

featureFileDir='myfeatures'
featureFile='parameterize.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

scenarios(FEATURE_FILE)

@given('there are 3 varieties of fruits', target_fixture='fruits')
def existing_fruits():
    fruits = {'apples', 'grapes', 'strawberry'}
    return fruits

@when('we add a same variety of fruit')
def add_a_fruit(fruits):
    fruits.add("grapes")

@then('there is same count of varieties')
def same_count(fruits):
    assert len(fruits) == 3

@then('if we add a different variety of fruit')
def add_diff_variety(fruits):
    fruits.add("cherry")

@then(parsers.parse('the count of varieties increases to {count:d}'))
def count_increase(fruits, count):
    print(fruits)
    assert len(fruits) == count

# End of first scenario

@given(parsers.parse('There are {count:d} fruits'), target_fixture='start_fruits')
def existing_fruits(count):
    return dict(start=count, eat=0)

@when(parsers.parse("I eat {eat:d} fruits"))
def eat_fruits(start_fruits, eat):
    start_fruits["eat"] += eat
    print(start_fruits)

@then(parsers.parse("I should have {left:d} fruits"))
def should_have_left_fruits(start_fruits, left):
    #assert start_fruits['start'] == count
    assert start_fruits['start'] - start_fruits['eat'] == left

