# test_model.py

import unittest
from model import train_model
from preprocess import clean_data
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

class TestModel(unittest.TestCase):
    def test_train_model(self):
        cleaned_data = clean_data("test_data.txt")

        # Creating labels based on the user's input
        labels = ['User' if i % 2 == 0 else 'Chatbot' for i in range(len(cleaned_data))]

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(cleaned_data, labels, test_size=0.2, random_state=42)

        # Train the model
        trained_model, _ = train_model(X_train)

        # Assertions for the training process
        self.assertIsNotNone(trained_model)
        self.assertIsInstance(trained_model, type(make_pipeline(CountVectorizer(), LogisticRegression())))

        # Check the model's accuracy using the testing set
        accuracy = trained_model.score(X_test, y_test)
        print(f"Model Accuracy: {accuracy:.2f}")
        print("---------------------")

        # Ensure accuracy is greater than or equal to 0.5
        self.assertGreaterEqual(accuracy, 0.5) 

# run test with: python -m unittest test_model.py
