# use pytest to test the add function in app.py
from app import add

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    from app import subtract
    assert subtract(2, 1) == 1
    assert subtract(1, 1) == 0
    assert subtract(0, 0) == 0
    

 # add main function to run the tests
if __name__ == "__main__":
    test_add()
    test_subtract()
    print("All tests passed!")