# import pandas module to parse csv dataset 
import pandas as pd

# define FuitBot Function
def FruitBot(input):
    # running loop through user's input and compare each word with fruits in dataset to find a match
    for item in input.split():
        # select each fruit from dataset to compare
        for index,data in clean_dataset.iterrows():
            # conditional statement to compare each word from user's input to each fruit in dataset
            if item.lower() == data['name'].lower():
                print(data['name'],'is a',data['type'],'and is',data['color'],'in color. It is',data['taste'],'in taste.')
             
print('Hey! ask me about any fruit in your mind')
# gets input from user
fruit = input('')
# reads csv file
dataset = pd.read_csv('fruit_dataset.csv')
clean_dataset = dataset.drop_duplicates()
# runs function 
FruitBot(fruit)