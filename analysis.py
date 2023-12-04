import statistics
import numpy as np
import matplotlib.pyplot as plt

def analyse_data(data):
    messageLengths = []
    wordcounts = []
    
    for s in data:
        messageLengths.append(len(s))
        wordcounts.append(len(s.split()))

    # Calculating and outputting statistics for length of messages
    meanLength = statistics.mean(messageLengths)
    medianLength = statistics.median(messageLengths)
    minLength = min(messageLengths)
    maxLength = max(messageLengths)
    print("Mean message length is", meanLength, "characters long")
    print("Median message length is", medianLength,"characters long")
    print("Maximum message length is", maxLength, "characters long")
    print("Minimum message length is", minLength,"characters long")
   
    # Calculating and outputting statistics for number of words
    meanWords = statistics.mean(wordcounts)
    medianWords = statistics.median(wordcounts)
    minWords = min(wordcounts)
    maxWords = max(wordcounts)
    print("Mean number of words is", meanWords, "words long")
    print("Median number of words is", medianWords,"words long")
    print("Maximum number of words is", maxWords, "words long")
    print("Minimum number of words is", minWords,"wordss long")
    
    boxplotData = [messageLengths, wordcounts]

    plt.boxplot(boxplotData, labels=("Message Length", "Wordcount"))
    plt.show()