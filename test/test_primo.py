import pytest

from src.primo import verify_primer_with_attempts

def test_verify_prime_number_two():
    is_prime, divisible = verify_primer_with_attempts(2)
    assert is_prime
    assert divisible == 1


def test_verify_prime_number_four():
    is_prime, divisible = verify_primer_with_attempts(4)
    assert not is_prime
    assert divisible == 2

def test_verify_prime_number_seven():
    is_prime, divisible =  verify_primer_with_attempts(7)
    assert is_prime
    print(divisible)
    assert divisible == 1


def test_verify_prime_number_twelve():
    is_prime, divisible =  verify_primer_with_attempts(12)
    assert not is_prime
    print(divisible)
    assert divisible == 2

def test_verify_prime_number_one_hundred_three():
    is_prime, divisible =  verify_primer_with_attempts(123)
    assert not is_prime
    print(divisible)
    assert divisible == 3