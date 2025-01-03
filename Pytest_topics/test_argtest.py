from Pytest_topics.conftest import cmdopt

def test_argtest01(cmdopt):
    print ("Read config file: " + cmdopt.readline())