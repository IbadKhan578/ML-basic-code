import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv(
    'C:/Users/DELL/Documents/Python/100 days of ML/placement.csv'
)

# Dataset overview
print("Dataset shape (rows, columns):", df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nDataset info:")
df.info()

print("\nStatistical summary:")
print(df.describe())

# Feature and target selection
X = df[['cgpa']]      # 2D array (best practice)
y = df['package']    # 1D target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=2
)

# Model training
model = LinearRegression()
model.fit(X_train, y_train)

# Model evaluation
print("\nModel coefficient:", model.coef_)
print("Model intercept:", model.intercept_)
print("Model score (R²):", model.score(X_test, y_test))

# Visualization
plt.figure(figsize=(8, 5))
sns.regplot(x='cgpa', y='package', data=df)
plt.title("CGPA vs Package")
plt.xlabel("CGPA")
plt.ylabel("Package")
plt.show()