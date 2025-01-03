from Pytest_topics.utils.myconfigparser import *
from Pytest_topics.utils.configFileParser import ConfigFileParser

config = ConfigFileParser('prod.ini')

def test_getgmailurl():
    print(getGmailURL())

def test_getoutlookurl():
    print(config.getoutlookurl())
