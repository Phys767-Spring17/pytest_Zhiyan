#file located in pytest_Zhiyan/
#filename = test_fizzbuzz.py

from fizzbuzz_Z import fizzbuzz
import pytest

#assert checks true/false
def test_fizzbuzz_1():
    assert fizzbuzz(1) == 1

def test_fizzbuzz_34():
    assert fizzbuzz(34) == 34

def test_fizzbuzz_3():
    assert fizzbuzz(3) == 'fizz'

def test_fizzbuzz_5():
    assert fizzbuzz(5) == 'buzz'

def test_fizzbuzz_33():
    assert fizzbuzz(33) == 'fizz'

def test_fizzbuzz_50():
    assert fizzbuzz(50) == 'buzz'

def test_fizzbuzz_15():
    assert fizzbuzz(15) == 'fizzbuzz'

def test_fizzbuzz_45():
    assert fizzbuzz(45) == 'fizzbuzz'

def test_fizzbuzz_90():
    assert fizzbuzz(90) == 'fizzbuzz'


def test_fizzbuzz_105():
    assert fizzbuzz(105) == 'fizzbuzz'
