def test_a1():
    print("This is my firs test")
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5 / 5 == 1

def test_a2():
    assert 9/5 == 1.5, "failed test intentionally"

def test_a3():
    assert 9//5 == 1 #integer truncating division

    #As note -> Always write testcase names with underscore. test_<something>.py
    #function name with test_<something>

