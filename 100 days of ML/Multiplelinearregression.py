import numpy as np 
import pandas as pd
import seaborn as sn
import plotly.express as px
from sklearn.datasets import make_regression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# sample data to practice regression
x,y = make_regression(n_samples=100, n_features=2, n_informative=2, n_targets=1,noise=50)
# x and y are array convert it to data framae 

df = pd.DataFrame({'feature1': x[:,0], 'feature2': x[:,1],'target':y})




print(df.head())
print('shape of the data is:', df.shape)

print(df.describe())

fig = px.scatter_3d(df, x='feature1', y='feature2',z='target')
# fig.show()

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=3 )

lr= LinearRegression()
lr.fit(x_train, y_train)  # train the model on training data 


y_pred = lr.predict(x_test)  
# x_test → the input features the model hasn’t seen
# y_pred → predicted target values



# R-squared (how much variance explained)
r2 = r2_score(y_test, y_pred)

# Mean Absolute Error (average absolute difference)
mae = mean_absolute_error(y_test, y_pred)

# Mean Squared Error (average squared difference)
mse = mean_squared_error(y_test, y_pred)

# Root Mean Squared Error (square root of MSE)
# rmse = mean_squared_error(y_test, y_pred, squared=False)

print('R2 score:', r2)
print('MAE:', mae)
print('MSE:', mse)
# print('RMSE:', rmse)