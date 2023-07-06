###########################
#This file contains the basic pandas functions
###########################
import pandas as pd
###########################
#Data frame
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
#the container is composed of a dictionary whose keys are the column names
# to name the rows we can use the function index which we give a list 
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
##########################
#Series
pd.Series([1, 2, 3, 4, 5])
#In this case the generator uses a list
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
#In this case we can just change the rows names and give a name for the wole series
##########################
#Reading data 
data=pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")
data.shape
data.head()
#This shows the first five rows

data_two = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
#index_col is important for when the rows were already named with an index list, that helps us avoid creating two
##########################
#To transform a dataframe into a csv file
data.to_csv("data_file.csv")

