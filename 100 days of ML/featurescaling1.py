import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Data
X = np.array([
    [25, 5000, 1.5],
    [30, 12000, 3.2],
    [45, 30000, 2.1],
    [35, 18000, 4.5],
    [60, 80000, 6.0]
])

df = pd.DataFrame(X, columns=["Age", "Income", "Experience"])

# Features and target
x = df[["Age", "Income"]]
y = df[["Experience"]]

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Standardization
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fit on training data
X_test_scaled = scaler.transform(X_test)        # transform test data
  

# Convert back to DataFrame
X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns)
X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns)

print("Standardized X_train:\n", X_train_scaled)
print("Standardized X_test:\n", X_test_scaled)
print("Mean of X_train_scaled:\n", X_train_scaled.mean().round(5))