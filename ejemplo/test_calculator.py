# test_calculator.py
import coverage

cov = coverage.Coverage()
cov.start()

def add_numbers(a, b):
    return a + b

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

if __name__ == "__main__":
    test_add_numbers()
    cov.stop()
    cov.save()
    cov.report()
