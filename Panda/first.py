import pandas as pd
import numpy as np 


# panda series 

# country = ["Pakistan", "India", "Australia", "UK", "USA"];

# print(pd.Series(country));   # series from a list 

# #Custom index

# marks=[60,66,90,84];
# subjects = ['English', 'Math','Physics','DSA'];
# print(pd.Series(marks,index=subjects)); # making subjects as index of the series 


mark={
    'English': 44,
    'Maths': 99,
    'Physics': 84,
    'DSA' : 77
    }
  # series from a dictionary 
pd.Series(mark) 

mark1 = pd.Series(mark) # mark1 is the object of this series, so  it will have attributes  too

# # series attributes 
# print(mark1.size)  # tell the number of items in the series 
# print(mark1.dtype)   # tells the data type of the series 
# print(mark1.is_unique)  # return true if the elements in the series are not repeating.
# print(mark1.index)   # return index of the series 
# print(mark1.values)  # return values of the series. 


# how to read csv files 
# val=pd.read_csv('Panda\subs.csv')
# print(type(val))  # by default it is data frame not series 
# to  convert it into series, we will run following command
val2= pd.read_csv('Panda\subs.csv').squeeze('columns')   # converted to series. 
# print(val2, type(val2));

val3 = pd.read_csv('Panda\kohli_ipl.csv', index_col='match_no').squeeze('columns');
# print(val3);

# series method 

# head method
# print(val3.head());   # return top 5 rows always.
# print(val3.head(3));  # we can also specify the required rows to be fetched.

# tail method

# print(val3.tail());   # return last 5 rows, we can also speicfy rows to be fetched.

# sample method

# print(val3.sample());  # return a random one row from the data 
# print(val3.sample(20)); # return a random 20 rows/sample  from the data 

# value_count method that return the frequency of the value appeared in the data.

# print(val3.value_counts())   # i.e V kohli got out 9 times on zero

# sort_values method  sorts values in ascending orders 

# print(val3.sort_values());  # sort in ascending order 
# # print(val3.sort_values(ascending=False));  # sort in desceding order 


# some math function  of series 

# print(val3.count()); # same as count function that return number of element, it does not count missing value

# sum method 
# print(val2, " The number of subscribers are:", val2.sum()); # sum of all values 


# # mean, mode , median , std, variance formula 
# print("Average subscriber in a day are: ",val2.mean())
# print("the median is: ", val2.median());  # the middle value in ordeered dataset 
# print("Mode is: ", val2.mode()); # most frequent or occuring value 
# print("Standard deviation is: ", val2.std()); # how spreaded data is from average 
# print("variance is: ", val2.var());


# # min/max function

# print("Min value is: ",val2.min())
# print("Max value is: ",val2.max());

# # describe function that describes data using mathametical function

# print("Desrciption of data is: ", val2.describe())


# series indexing 

# numbers= [1,2,3,6,3,6,5,7,3];
# numb = pd.Series(numbers)
# print(numb[7]) # return element at 8th index(series does not work on neg index)


# Slicing

# print(val3[5:16]); # return data from 5 to 15 

# Neg slicing

# print(val3[-5:])  # return last 5 values 


#  Editing series 

# val3[2]=77;
# print(val3)


# important series method 

#astype -> change the data type of the series 

# between method 
# between() returns True for values that fall within a specified range and False for those that do not.
# print(val3.between(10,20))

# clip method
# In pandas, the clip() function is used to limit values within a given range.
# Values smaller than the minimum are raised to the minimum, and values larger than the maximum are reduced to the maximum

# print(val3.clip(50,100))


# Drop duplicates 

temp= pd.Series([1,2,3,2,4,3,2,1,np.nan])
# print(temp.drop_duplicates())   # drop duplicates 
# print(temp.duplicated().sum())  # sum of duplicates item


# is null 

# print(temp.isnull().sum())   # tell how many values are null


# print(temp.dropna())   # drop null value row 

# fillna 

# print(temp.fillna(3)); # replace null value to 3
# print(temp.fillna(temp.mean())); # replace null value with mean
