import numpy as np
import pandas as pd 

# understanding your data 


url= "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df= pd.read_csv(url);


# 1- how big the data is ?
print(df.shape) # (891,12)

# 2- how does the data look like?
print(df.head())


#  3- what are the data types of the columns 

print(df.info())   



# - 4 are there any missing value??

print(df.isnull().sum()) # it tells how many null values are in each column 


# -5 how does the data look mathematically 

print(df.describe())


# 6- are there any duplicated values??

print(df.duplicated().sum())  # tells if there are any duplicates values 


#   6- how is the correlation between cols 

print(df.corr(numeric_only=True)['Survived']); # tells whether the cols have any relation between them
# positive reltion means strong relation and neg means weak

