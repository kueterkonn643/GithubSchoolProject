import numpy as np
from sklearn.model_selection import train_test_split

data = [1.0, 2.0, 3.0]  # Replace with your actual data points
labels = [1, 0, 1]      # Replace with the corresponding labels for each data point

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
