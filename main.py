from preprocess import clean_data 
from analysis import analyse_data
from model import train_model

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
    
    trained_model = train_model(cleaned_data)