# model.py

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import pandas as pd

def train_model(data):
    # Creating labels based on the user's input
    labels = ['User' if i % 2 == 0 else 'Chatbot' for i in range(len(data))]

    # Splitting the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

    # Creating a pipeline with a Bag-of-Words model and Logistic Regression
    model = make_pipeline(CountVectorizer(), LogisticRegression())
    
    # Training the model
    model.fit(X_train, y_train)

    # Evaluating the model
    accuracy = model.score(X_test, y_test)
    print(f"Model Accuracy: {accuracy:.2f}")
    print("---------------------")
    return model, labels
