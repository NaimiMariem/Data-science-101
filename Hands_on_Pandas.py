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
##########################
#Indexing
##########################
df.column_name
#or
df["column_name]
#Show just one element
df["column"].[i]
##########################
#Pandas accesor operators
# loc and iloc
#iloc uses the index which means it shows the row corresponding to the index given
df.iloc[o]
#This gives us the first row
#### Both loc and iloc are row-first, column-second ######
df.iloc[:, 0]  # This enables us to access the first column
df.iloc[list,i] #works too
#Label based selection is also possible
df.loc[0,"column_name"] # thsi for example gives te first element of teh column_name
df.loc[:,['column_name1','column_name2','column_name3','column_name4']] #extracts the data for chosen columns

###iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded.
#####So 0:10 will select entries 0,...,9. loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.
#We can also use conditonal indexing to generate a liste of boolean data (true/false)
df.columun_name==data_of_interest #this generates a list where it says if th elements of each row of the column "column_name" is equal to teh dta aof interest of not
# Another interesting method is selcting all the data based on a dat of interest
#example
df.loc[df.column_name==data_of interest]
#askip iloc requires only numerical indexes

#####To combine filtering conditions in Pandas, use bitwise operators ('&' and '|') not pure Python ones ('and' and 'or')
##########################
# describe is a good function to reshape data but it only is relevenat for numerical data 
#### To get the list of values for a cerftain feature
df.column_name.unique()
## How often does each value appear 
df.column_name.value_counts()

### The function map uses a function to apply it to all the values 
#example
mean_feature=df.column_name.mean()
df.column_name.map( lambda p : p- mean_feature) # In the example we retrive the mean  value of the feature selected from all the corresponding values

###### the function groupby can be used to have an extract with rows that are categorized according to a cerftain feature (column_name) 
df.groupby("column_name").another_feature()
#will have an extract of the dataset with rows of unique elements of column_name 
# in the second column will have the "other feature" for each elements
#Another example 
df.groupby('column_name').apply(lambda df: df.column_name_2.iloc[0])
# Let column_name be= house_type and column_name_2= owner , this case the command line will return the first owner in the dataset in each different type of house
#####Another groupby() method worth mentioning is agg(), which lets you run a bunch of different functions on your DataFrame simultaneously. 
######For example, we can generate a simple statistical summary of the dataset as follows:
df.groupby(['column_name']).feature.agg([len, min, max]) #ofc specify the feature
#######Another important specification about the groupby function is that it allolws us to have multi_indexes 
#i.e you can have two rows f rows lool 
df_multii=df.groupby(['column_name_1','column_name_2']).feature.agg([functions_list])
#let column_name_1 be country and column_name_2 be province 
# will have each feature for each province organized by country !
## pandas.core.indexes.multi.MultiIndex (type of variable)
# The problem is, this is hard to adress elements when we have this system of indexing 
# So we need to reorganize it 
df_sorted=df_multi.reset.index()
#Sorting 
df_sorted.sort_values(by='column_name')
#In order to have the higher values first
df_sorted.sort_values(by='column_name',ascending= False)

########################################
##Data type
########################################
#The data type for a column in a DataFrame or a Series is known as the dtype
df.column_name.dtype
#Return example dype("float64")
df.dtype #Gives the dtype of every column
#If a conversion of type makes sense we can do it using astype 
df.column_name.astype("float64")
#######################################
#Missing data 
#######################################
#Missing data are given the NaN value (float64 dtype)
df[pd.isnull(df.column_name)]
#replacing missing values with another 
df.column_name.fillna("Unknown") #There are different ways of replacing missing values
#Replacing a value with another
df.column_name.replace("value1","value2")
