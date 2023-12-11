import unittest
from analysis import analyse_data

class TestAnalyseData(unittest.TestCase):

    def test_mean_message_length(self):
        with open("test_data.txt", "r", encoding="utf-8") as file:
            test_data = file.readlines()
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        analyse_data(test_data)
        sys.stdout = sys.__stdout__  
        output_lines = captured_output.getvalue().split('\n')
        # assertion for mean message length
        self.assertIn("Mean message length is", output_lines[0])
        
    def test_median_message_length(self):
        with open("test_data.txt", "r", encoding="utf-8") as file:
            test_data = file.readlines()
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        analyse_data(test_data)
        sys.stdout = sys.__stdout__  
        output_lines = captured_output.getvalue().split('\n')
        # assertion for median message length
        self.assertIn("Median message length is", output_lines[1])

    def test_maximum_message_length(self):
        with open("test_data.txt", "r", encoding="utf-8") as file:
            test_data = file.readlines()
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        analyse_data(test_data)
        sys.stdout = sys.__stdout__  
        output_lines = captured_output.getvalue().split('\n')
        # assertion for maximum message length
        self.assertIn("Maximum message length is", output_lines[2])

    def test_minimum_message_length(self):
        with open("test_data.txt", "r", encoding="utf-8") as file:
            test_data = file.readlines()
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        analyse_data(test_data)
        sys.stdout = sys.__stdout__  
        output_lines = captured_output.getvalue().split('\n')
        # assertion for minimum message length
        self.assertIn("Minimum message length is", output_lines[3])

    def test_mean_number_of_words(self):
        with open("test_data.txt", "r", encoding="utf-8") as file:
            test_data = file.readlines()
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        analyse_data(test_data)
        sys.stdout = sys.__stdout__ 
        output_lines = captured_output.getvalue().split('\n')
        # assertion for mean number of words
        self.assertIn("Mean number of words is", output_lines[4])

    def test_median_number_of_words(self):
        with open("test_data.txt", "r", encoding="utf-8") as file:
            test_data = file.readlines()
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        analyse_data(test_data)
        sys.stdout = sys.__stdout__  
        output_lines = captured_output.getvalue().split('\n')
        # assertion for median number of words
        self.assertIn("Median number of words is", output_lines[5])

    def test_maximum_number_of_words(self):
        with open("test_data.txt", "r", encoding="utf-8") as file:
            test_data = file.readlines()
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        analyse_data(test_data)
        sys.stdout = sys.__stdout__  
        output_lines = captured_output.getvalue().split('\n')
        # assertion for maximum number of words
        self.assertIn("Maximum number of words is", output_lines[6])

    def test_minimum_number_of_words(self):
        with open("test_data.txt", "r", encoding="utf-8") as file:
            test_data = file.readlines()
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        analyse_data(test_data)
        sys.stdout = sys.__stdout__ 
        output_lines = captured_output.getvalue().split('\n')
        # assertion for minimum number of words
        self.assertIn("Minimum number of words is", output_lines[7])

# python -m unittest -v test_analysis.py
