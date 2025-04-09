import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = np.random.rand(100, 2)  # Generate some random data with 100 samples and 2 features
plt.scatter(data[:, 0], data[:, 1])  # Plot the scatter plot of the data
plt.title("Scatter Plot of Data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

model = LinearRegression()  # Create a linear regression model
model.fit(data, np.ones(data.shape[0]))  # Train the model on the data

coefficients = model.coef_[0]  # Extract the coefficients from the model
intercept = model.intercept_

print(f"Linear Regression Coefficients: {coefficients}")
print(f"Intercept: {intercept}")

plt.show()  # Show the scatter plot and the regression line
