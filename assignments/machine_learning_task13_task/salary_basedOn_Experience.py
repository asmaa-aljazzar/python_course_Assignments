import pandas as pd
df = pd.read_csv ("salary_data.csv")

# Split features and target
x = df['YearsExperience']
y = df['Salary']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split (x, y, test_size = 0.2, random_state = 42)

x_train_reshaped = x_train.values.reshape (-1, 1)

from sklearn.linear_model import LinearRegression
# Train the linear regression model
model = LinearRegression ()
model.fit (x_train_reshaped, y_train)

x_test_reshaped = x_test.values.reshape (-1, 1)
y_pred = model.predict (x_test_reshaped)

from sklearn.metrics import mean_squared_error, r2_score


mse = mean_squared_error (y_test, y_pred)
r2 = r2_score (y_test, y_pred)

print (f"Mean Squares Error: {mse: .2f}")
print (f"R² Sqore: {r2: .2f}")

import matplotlib.pyplot as plt
plt.figure (figsize = (5, 5))
plt.scatter (x, y, color = 'purple', label = 'Actual Data')
plt.plot (x_test, y_pred, color = 'orange', linewidth = 3, label = 'Regression Line')
plt.title ("Years of Experience")
plt.xlabel ("Salary")
plt.grid (True) # With grid
plt.legend ()
plt.show ()
#_____________________________________________________________________________________
plt.figure (figsize = (5, 5))
plt.scatter (x, y, color = 'purple', label = 'Actual Data')
plt.plot (x_test, y_pred, color = 'orange', linewidth = 3, label = 'Regression Line')
plt.title ("Years of Experience")
plt.xlabel ("Salary")
plt.grid (False) # Without grid
plt.legend ()
plt.show ()