import unittest
from check_prime import is_prime  

class TestPrime(unittest.TestCase):
    def test_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(101))

    def test_non_primes(self):
        self.assertFalse(is_prime(1))  # Edge 
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(0))  # Edge 

    def test_negative_numbers(self):
        self.assertFalse(is_prime(-1))  # Edge 
        self.assertFalse(is_prime(-7))

    def test_large_primes(self):
        self.assertTrue(is_prime(7919))
        self.assertTrue(is_prime(104729))

    def test_large_non_primes(self):
        self.assertFalse(is_prime(8000))
        self.assertFalse(is_prime(104730))

if __name__ == "__main__":
    unittest.main()
