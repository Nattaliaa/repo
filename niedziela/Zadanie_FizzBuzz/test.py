from app import *

def test_0():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(4) == 4
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(0) == 0
    assert fizzbuzz(-3) == None