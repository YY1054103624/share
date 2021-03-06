import pytest


@pytest.mark.set1
def test_file1_method1():
    x = 5
    y = 6
    assert x + 1 == y, "test failed because x=" + str(x) + " y=" + str(y)
    assert x == y, "test failed because x=" + str(x) + " y=" + str(y)


@pytest.mark.set2py
def test_file1_method2():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"
