import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read the spreadsheet
data = pd.read_excel(r'C:\Users\walzk01\Downloads\baseball.xlsx')

# First regression: Wins vs. Runs Scored - Runs Allowed
X1 = data['Runs Scored'] - data['Runs Allowed']
y1 = data['Wins']
X1 = sm.add_constant(X1)  # Add a constant term to the independent variable
model1 = sm.OLS(y1, X1).fit()  # Perform linear regression
r_squared1 = model1.rsquared  # Get the R-squared value

# Visualize the data and regression line
plt.scatter(X1[:, 1], y1)
plt.plot(X1[:, 1], model1.predict(X1), color='red')
plt.xlabel('Runs Scored - Runs Allowed')
plt.ylabel('Wins')
plt.title('Wins vs. Runs Scored - Runs Allowed')
plt.text(0.05, 0.95, f'R-squared: {r_squared1:.2f}', transform=plt.gca().transAxes)
plt.show()

# Second regression: Runs Scored - Runs Allowed vs. Team Batting Average
X2 = data['Team Batting Average']
y2 = data['Runs Scored'] - data['Runs Allowed']
X2 = sm.add_constant(X2)  # Add a constant term to the independent variable
model2 = sm.OLS(y2, X2).fit()  # Perform linear regression
r_squared2 = model2.rsquared  # Get the R-squared value

# Visualize the data and regression line
plt.scatter(X2[:, 1], y2)
plt.plot(X2[:, 1], model2.predict(X2), color='red')
plt.xlabel('Team Batting Average')
plt.ylabel('Runs Scored - Runs Allowed')
plt.title('Runs Scored - Runs Allowed vs. Team Batting Average')
plt.text(0.05, 0.95, f'R-squared: {r_squared2:.2f}', transform=plt.gca().transAxes)
plt.show()

# Third regression: Runs Scored - Runs Allowed vs. OBP and SLG
X3 = data[['OBP', 'SLG']]
y3 = data['Runs Scored'] - data['Runs Allowed']
X3 = sm.add_constant(X3)  # Add a constant term to the independent variables
model3 = sm.OLS(y3, X3).fit()  # Perform multiple regression
r_squared3 = model3.rsquared  # Get the R-squared value

# Print regression statistics
print(model3.summary())

# Explanation of regression statistics:
# R-squared: The proportion of variance in the dependent variable that is predictable from the independent variables.

# Go Yankees!