import unittest
from calc_prime_numbers import gen_prime_numbers

class test_generate_prime_numbers(self):
    def test_prime_output(self):
        self.assertEqual(gen_prime_numbers(20),[ 2, 3, 5, 7, 11, 13, 17, 19])
    def test_input_string(self):
        self.assertEqual(gen_prime_numbers('string'),"Please input a number")
    def test_output_is_list(self):
        self.assertEqual(gen_prime_numbers(20),list)
##    def test_output_for_negative_input(self):
##        self.assertEqual(gen_prime_numbers(-2),'No negative prime numbers')
        
unittest.main()
