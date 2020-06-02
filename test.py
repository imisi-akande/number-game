# For running unit tests, use
# python -m unittest -v test.py

import unittest

from nummer_games import Generation
from nummer_games import Classify
from nummer_games import Prime
from unittest.mock import patch
import random

class TestClassifyClass(unittest.TestCase):
    def setUp(self):
        self.user_one = Generation(3)

    def get_log_text(self, logs_list):
        return ' '.join(logs_list)

    def test__initialization(self):
        self.assertNotEqual(self.user_one.n, 2, 'incorrect number of attempts')
        self.assertEqual(self.user_one.n, 3)

    @patch('builtins.input', return_value=20)
    def test__guess_number_once__you_right(self, input_mock):
        with self.assertLogs() as cm:
            random.seed(900)
            guess = Classify(1).guess_number()

        input_mock.assert_called_once()
        self.assertIn('Congratulation YOU WON', self.get_log_text(cm.output))

    @patch('builtins.input', side_effect=[11, 20])
    def test__guess_number_twice__you_right(self, input_mock):
        with self.assertLogs() as cm:
            random.seed(900)
            guess = Classify(2).guess_number()

        self.assertEqual(input_mock.call_count, 2)

        log_text = self.get_log_text(cm.output)
        self.assertIn('Your guess is too low', log_text)
        self.assertIn('Congratulation YOU WON', log_text)

    @patch('builtins.input', side_effect=[11, 31, 20])
    def test__guess_number_thrice__you_right(self, input_mock):
        with self.assertLogs() as cm:
            random.seed(900)
            guess = Classify(3).guess_number()

        self.assertEqual(input_mock.call_count, 3)

        log_text = self.get_log_text(cm.output)
        self.assertIn('Your guess is too low', log_text)
        self.assertIn('Your guess is too high', log_text)
        self.assertIn('Congratulation YOU WON', log_text)

    @patch('builtins.input', return_value=20)
    def test__guess_number_right__on_first_attempt(self, input_mock):
        with self.assertLogs() as cm:
            random.seed(900)
            guess = Classify(3).guess_number()

        input_mock.assert_called_once()
        self.assertIn('Congratulation YOU WON', self.get_log_text(cm.output))

    @patch('builtins.input', side_effect=[31, 20])
    def test__guess_number_right__on_second_attempt(self, input_mock):
        with self.assertLogs() as cm:
            random.seed(900)
            guess = Classify(3).guess_number()

        self.assertEqual(input_mock.call_count, 2)

        log_text = self.get_log_text(cm.output)
        self.assertIn('Your guess is too high', log_text)
        self.assertIn('Congratulation YOU WON', log_text)

    @patch('builtins.input', side_effect=[21, 15, 20])
    def test__guess_number_right__on_third_attempt(self, input_mock):
        with self.assertLogs() as cm:
            random.seed(900)
            guess = Classify(3).guess_number()

        self.assertEqual(input_mock.call_count, 3)

        log_text = self.get_log_text(cm.output)
        self.assertIn('Your guess is too high', log_text)
        self.assertIn('Your guess is too low', log_text)
        self.assertIn('Congratulation YOU WON', log_text)

    @patch('builtins.input', return_value=10)
    def test__guess_number_once__you_wrong(self, input_mock):
        with self.assertLogs() as cm:
            random.seed(900)
            guess = Classify(1).guess_number()

        input_mock.assert_called_once()
        self.assertIn('Sorry.. YOU LOSE!!!', self.get_log_text(cm.output))

    @patch('builtins.input', side_effect=[11, 18])
    def test__guess_number_twice__you_wrong(self, input_mock):
        with self.assertLogs() as cm:
            random.seed(900)
            guess = Classify(2).guess_number()

        self.assertEqual(input_mock.call_count, 2)

        log_text = self.get_log_text(cm.output)
        self.assertIn('Your guess is too low', log_text)
        self.assertIn('Sorry.. YOU LOSE!!!', log_text)

    @patch('builtins.input', side_effect=[11, 31, 18])
    def test__guess_number_thrice__you_wrong(self, input_mock):
        with self.assertLogs() as cm:
            random.seed(900)
            guess = Classify(3).guess_number()

        self.assertEqual(input_mock.call_count, 3)

        log_text = self.get_log_text(cm.output)
        self.assertIn('Your guess is too low', log_text)
        self.assertIn('Your guess is too high', log_text)
        self.assertIn('Sorry.. YOU LOSE!!!', log_text)


class TestPrimeClass(unittest.TestCase):
    def setUp(self):
        self.user_one = Generation(3)

    def get_log_text(self, logs_list):
        return ' '.join(logs_list)

    def test__initialization(self):
        self.assertNotEqual(self.user_one.n, 2, 'incorrect number of attempts')
        self.assertEqual(self.user_one.n, 3)

    @patch('builtins.input', return_value=13)
    def test__guess_prime_number_once__you_right(self, input_mock):
        with self.assertLogs() as cm:
            guess = Prime(1).guess_prime_number()

        input_mock.assert_called_once()
        self.assertIn('13, is a prime number', self.get_log_text(cm.output))

    @patch('builtins.input', side_effect=[23, 43])
    def test__guess_prime_number_twice__you_right(self, input_mock):
        with self.assertLogs() as cm:
            guess = Prime(2).guess_prime_number()

        self.assertEqual(input_mock.call_count, 2)

        log_text = self.get_log_text(cm.output)
        self.assertIn('23, is a prime number', log_text)
        self.assertIn('43, is a prime number', log_text)
        self.assertIn('2 attempts succesfully made', log_text)

    @patch('builtins.input', side_effect=[23, 43, 73])
    def test__guess_prime_number_thrice__you_right(self, input_mock):
        with self.assertLogs() as cm:
            guess = Prime(3).guess_prime_number()

        self.assertEqual(input_mock.call_count, 3)

        log_text = self.get_log_text(cm.output)
        self.assertIn('23, is a prime number', log_text)
        self.assertIn('43, is a prime number', log_text)
        self.assertIn('73, is a prime number', log_text)
        self.assertIn('3 attempts succesfully made', log_text)

    @patch('builtins.input', return_value=12)
    def test__guess_prime_number_once__you_wrong(self, input_mock):
        with self.assertLogs() as cm:
            guess = Prime(1).guess_prime_number()

        input_mock.assert_called_once()
        self.assertIn('12,is not a prime number', self.get_log_text(cm.output))

    @patch('builtins.input', side_effect=[22, 44])
    def test__guess_prime_number_twice__you_wrong(self, input_mock):
        with self.assertLogs() as cm:
            guess = Prime(2).guess_prime_number()

        self.assertEqual(input_mock.call_count, 2)

        log_text = self.get_log_text(cm.output)
        self.assertIn('22,is not a prime number', log_text)
        self.assertIn('44,is not a prime number', log_text)
        self.assertIn('2 attempts succesfully made', log_text)

    @patch('builtins.input', side_effect=[22, 44, 100])
    def test__guess_prime_number_twice__you_wrong(self, input_mock):
        with self.assertLogs() as cm:
            guess = Prime(3).guess_prime_number()

        self.assertEqual(input_mock.call_count, 3)

        log_text = self.get_log_text(cm.output)
        self.assertIn('22,is not a prime number', log_text)
        self.assertIn('44,is not a prime number', log_text)
        self.assertIn('100,is not a prime number', log_text)
        self.assertIn('3 attempts succesfully made', log_text)


if __name__ == '__main__':
    unittest.main()