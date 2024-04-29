# importing necessary modules
from preprocess import clean_data 
from analysis import analyse_data
import matplotlib.pyplot as plt
import random
import tkinter as tk
import keystrings
import nltk
from tkinter import *

# defining application class
class App(tk.Tk):
    # initialising application
    def __init__(self, nouns):
        # call to superclass constructor
        super().__init__()
        # initialising endLoop as false
        self.endLoop = False
        # assign noun list
        self.nouns = nouns
        
        # setting window size 
        self.geometry("500x700")
        # setting window title
        self.title("Chatbot")
        # create frame
        topFrame = Frame (self)
        bottomFrame = Frame(self)
        # creating box dimensions
        outputBox = Text(topFrame, height = 30,
                    width = 55,
                    bg = "light cyan",
                    spacing1 = 5,
                    wrap="word")

        inputBox = Text(bottomFrame, height = 2, 
                width = 40, 
                bg = "light yellow",
                wrap="word")
        
        # creating button
        enterButton = Button(bottomFrame, height = 2,
                    width = 15, 
                    text ="Send",
                    command = lambda:get_input(self))
        
        # putting input and output into the boxes
        self.inputBox = inputBox
        self.outputBox = outputBox
        # bind return key to input box
        inputBox.bind("<Return>", key_pressed)
        # packing frames and boxes
        topFrame.pack()
        bottomFrame.pack()
        outputBox.pack()
        inputBox.pack(side = LEFT)
        enterButton.pack(side = LEFT)

        # welcome message into text box
        outputBox.insert(END, "Chatbot: Hi! How can I assist you with gift recommendations today?\n")
        outputBox.configure(state="disabled")
        
    # gets the input
    def get_inputBox(self):
        return self.inputBox
    # gets the reply
    def get_outputBox(self):
        return self.outputBox
    # gets endLoop
    def get_endLoop(self):
        return self.endLoop
    # gets list of nouns
    def get_nouns(self):
        return self.nouns
    
    # sets endLoop
    def set_endLoop(self, endLoop):
        self.endLoop = endLoop
    
# function for when key is pressed
def key_pressed(event):
    print(event.char)
    get_input(Tk.winfo_toplevel(event.widget))
    return 'break'
    
# function to get user input
def get_input(app):
    inputBox = app.get_inputBox()
    outputBox = app.get_outputBox()
    endLoop = app.get_endLoop()

    # getting input from the text box
    input = inputBox.get("1.0", "end-1c")
    inputBox.delete("1.0", "end-1c")
    outputBox.configure(state="normal")

    # displays user input to text box
    outputBox.insert(END, "You: " + input + "\n")

# checks if user input contains end_keywords
    if endLoop == True and (input.lower() in keystrings.end_keywords):
        outputBox.insert(END, "Chatbot: Goodbye!\n")
        app.quit()
    
# checks if user input contains exit keywords
    if input.lower() in keystrings.exit_keywords:
        outputBox.insert(END, "Chatbot: Is there anything else I can help you with today?\n")
        # then sets endLoop to true
        app.set_endLoop(True)    

    # if endLoop not set
    elif endLoop == False:
        # checks over keywords
        for keyword in keystrings.user_keywords:
            # checks if input contains keyword
            if keyword in input.lower():
                # generates random response
                response = "Chatbot: I would recommend " + random.choice(nouns)
                # inserts response to output box
                outputBox.insert(END, response + "\n")
                break

        # if input does not contain keyword
        else:
            # outputs a default message
            response = "Chatbot: I'm here to help with gift recommendations. Ask me anything!"
            # inserts response to output box
            outputBox.insert(END, response + "\n")
    else:
        response = "Chatbot: I'm a simple chatbot. You said something, and I'm responding."
        outputBox.insert(END, response + "\n")
    
    # disabling changes to texts  
    outputBox.configure(state="disabled")

if __name__ == "__main__":
    endLoop = False
    # cleaning dataset
    cleaned_data = clean_data("whatsapp.txt")
    # prompt for displaying analysis
    answer = input("Do you want an analysis of the corpus? Y/N: ")
    if answer == "Y":
        # analysing cleaned dataset
        analyse_data(cleaned_data)
        print("---------------------")

        # plotting analysis 
        plt.ion()
        plt.ioff()
        # displaying plots
        plt.show()
    
    # initialising noun list
    nouns = [] 
    for sentence in cleaned_data:
        # tagging words
        tagged_lines = nltk.pos_tag(nltk.word_tokenize(sentence))  
        # extracting quadgrams 
        quadgrams = nltk.ngrams(tagged_lines, 4)
        for (word1, tag1), (word2, tag2), (word3, tag3), (word4, tag4) in quadgrams:
            # converting to lowercase
            wordList = [word1.lower(), word2.lower(), word3.lower(), word4.lower()]
            # check if keyword "gift" and "present" are not in word list
            if "gift" not in wordList and "present" not in wordList:
                # checking for patterns in text
                if ((word1.lower() in ["a", "an"]) and tag2 + tag3 + tag4 in keystrings.text_patterns):
                    nouns.append(word1.lower() + " " + word2 + " " + word3 + " " + word4)
                elif ((word1.lower() in ["a", "an"]) and tag2 + tag3 in keystrings.text_patterns):
                    nouns.append(word1.lower() + " " + word2 + " " + word3)
                elif ((word1.lower() in ["a", "an"]) and tag2 in keystrings.text_patterns):
                    nouns.append(word1.lower() + " " + word2)

    # creating instance of app class                       
    app = App(nouns)
    # running application
    app.mainloop()
    # destroying app window
    app.destroy()
