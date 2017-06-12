import unittest
from calc_prime_numbers import prime

class test_generate_prime_numbers(unittest.TestCase):
    def test_prime_output(self):
        self.assertEqual(prime(6),[ 2, 3, 5])
    def test_string (self):
        self.assertEqual(prime('string'),"Invalid Input")
    def test_output_list(self):
        self.assertTrue(isinstance(prime(6),list))
    def test_output_negatives(self):
        self.assertEqual(prime(-2),'no negative prime numbers')
    def test_output_non_primes(self):
        self.assertNotIn([0,1,4,6],prime(6))
    
    
    


    
unittest.main()
