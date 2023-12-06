import unittest
from preprocess import clean_data

class TestCleanData(unittest.TestCase):
        # Case 1: testing with sample data file
    def test_clean_data_length(self):
        cleaned_data = clean_data("test_data.txt")
        self.assertGreater(len(cleaned_data), 0)
    def test_clean_data_outputs_list(self):
        cleaned_data = clean_data("test_data.txt")
        self.assertIsInstance(cleaned_data, list)
    def test_clean_data_output_length(self):
        cleaned_data = clean_data("test_data.txt")
        self.assertGreater(len(cleaned_data), 0)

        # Case 2: testing an empty data file
    def test_empty_data_not_none(self):
        cleaned_empty_data = clean_data("empty_data.txt")
        self.assertIsNotNone(cleaned_empty_data)
    def test_empty_data_outputs_list(self):
        cleaned_empty_data = clean_data("empty_data.txt")
        self.assertIsInstance(cleaned_empty_data, list)
    def test_empty_data_output_length(self):
        cleaned_empty_data = clean_data("empty_data.txt")
        self.assertEqual(len(cleaned_empty_data), 0)

        # Case 3: testing data containing special characters
    def test_special_chars_not_none(self):
        cleaned_special_chars = clean_data("test_data.txt")
        self.assertIsNotNone(cleaned_special_chars)
    def test_special_chars_outputs_list(self):
        cleaned_special_chars = clean_data("test_data.txt")
        self.assertIsInstance(cleaned_special_chars, list)
    def test_special_chars_output_length(self):
        cleaned_special_chars = clean_data("test_data.txt")
        self.assertGreater(len(cleaned_special_chars), 0)
    def test_special_chars_no_special_characters(self):
        cleaned_special_chars = clean_data("test_data.txt")
        self.assertNotRegex(cleaned_special_chars[0], r"[@#\\$%^&*()]+")

# command to run tests: python -m unittest -v test_preprocess.py
