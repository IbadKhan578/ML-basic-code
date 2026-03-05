import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 

# univariate analysis 
# where you analyze only one variable at a time


url= "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df= pd.read_csv(url)
print(df.head())


# 1) CATEGORICAL DATA   

#a) Count plot  ( create bar plots that display the frequency or count of a  category in a dataset.)


sns.countplot(x='Survived', data=df)  # how many survived
sns.countplot(df['Sex']) # how many were male n female
# plt.show();


# b) pie chart   ==> tells count in percentage 
df['Sex'].value_counts().plot(kind='pie',autopct='%.2f') # tells how much % were male n female 
# plt.show();



# 2) NUMERICAL DATA

# a- histogram
ages= df['Age']
plt.hist(ages, bins=20, color='skyblue', edgecolor='black')
plt.show()


