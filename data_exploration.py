import pandas as pd
from sklearn.tree import DecisionTreeRegressor


ex_file_path = '../input/path.csv'
ex_data = pd.read_csv(ex_file_path) #read the dataset 
ex_data.columns #Show teh columns used in the dataset
# Selecting a target with dot.notation
y=ex_data.column_name 
ex_features=["column_name_1","column_name_2","column_name_3","column_name_4"]  #Choosing the features that we'll use
X=ex_data[ex_features] #extract of the dataset
X.describe() #to print the extracted data 
X.head() #shows the first rows

# Define model. Specify a number for random_state to ensure same results each run
ex_model = DecisionTreeRegressor(random_state=1)

# Fit model
ex_model.fit(X, y)
# the prediction will concern the data in column y 
print("Making predictions for the following 5 xxx:")
print(X.head())
print("The predictions are")
print(ex_model.predict(X.head()))
