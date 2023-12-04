from preprocess import clean_data 
from analysis import analyse_data
from model import train_model
import matplotlib.pyplot as plt
import random

def chat_with_user(model, cleaned_data_lines, labels):
    print("Chatbot: Hi! How can I assist you with gift recommendations today?")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        predicted_label = model.predict([user_input])[0]

        if predicted_label == 'User':
            user_keywords = ['gift', 'present', 'recommendations', 'suggestions'] 
            for keyword in user_keywords:
                if keyword in user_input.lower():
                    relevant_chatbot_responses = [cleaned_data_lines[i] for i, label in enumerate(labels) if label == 'Chatbot']
                    response = "Chatbot: " + random.choice(relevant_chatbot_responses)
                    print(response)
                    break
            else:
                response = "Chatbot: I'm here to help with gift recommendations. Ask me anything!"
                print(response)
        elif predicted_label == 'Chatbot':
            response = "Chatbot: I'm a gift recommendation expert! Feel free to ask for suggestions."
            print(response)
        else:
            response = "Chatbot: I'm a simple chatbot. You said something, and I'm responding."
            print(response)

if __name__ == "__main__":
    cleaned_data = clean_data("whatsapp.txt")
    line = 0
    for x in cleaned_data:
        line = line + 1
        print(line, x, sep=": ")
    print("Data has been cleaned")
    print("---------------------")
    
    analyse_data(cleaned_data)
    print("---------------------")

    plt.ion()
    
    trained_model, labels = train_model(cleaned_data)

    chat_with_user(trained_model, cleaned_data, labels)
    
    plt.ioff()
    plt.show()