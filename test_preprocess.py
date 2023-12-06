import unittest
from preprocess import clean_data

class TestCleanData(unittest.TestCase):
    def test_clean_data(self):
        # Case 1: testing with sample data file
        cleaned_data = clean_data("test_data.txt")
        self.assertIsNotNone(cleaned_data)
        self.assertIsInstance(cleaned_data, list)
        self.assertGreater(len(cleaned_data), 0)
        print("Test 1: Passed")

        # Case 2: testing an empty data file
        cleaned_empty_data = clean_data("empty_data.txt")
        self.assertIsNotNone(cleaned_empty_data)
        self.assertIsInstance(cleaned_empty_data, list)
        self.assertEqual(len(cleaned_empty_data), 0)
        print("Test 2: Passed")

        # Case 3: testing data containing special characters
        cleaned_special_chars = clean_data("test_data.txt")
        self.assertIsNotNone(cleaned_special_chars)
        self.assertIsInstance(cleaned_special_chars, list)
        self.assertGreater(len(cleaned_special_chars), 0)
        self.assertNotRegex(cleaned_special_chars[0], r"[@#\\$%^&*()]+")  # Updated pattern to allow '!'
        print("Test 3: Passed")

# command to run tests: python -m unittest -v test_preprocess.py
