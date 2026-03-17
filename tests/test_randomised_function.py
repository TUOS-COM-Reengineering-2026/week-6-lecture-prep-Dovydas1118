import unittest
from unittest.mock import patch
from lecture import randomised_function

class MyTestCase(unittest.TestCase):

    @patch("lecture.randomised_function")
    def test_randomised_function_with_mock1(self, randomised_function_mock):
        randomised_function_mock.return_value = 'software'
        self.assertEqual(randomised_function_mock(), 'software')

    @patch("lecture.randomised_function")
    def test_randomised_function_with_mock2(self, randomised_function_mock):
        randomised_function_mock.return_value = 'engineering'
        self.assertEqual(randomised_function_mock(), 'engineering')