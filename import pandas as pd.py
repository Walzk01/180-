import pandas as pd

# Read the spreadsheet into a DataFrame
data = pd.read_excel(r'C:\Users\Katie\Downloads\baseball.xlsx')

# Select the required columns
selected_columns = ['Runs Scored', 'Runs Allowed', 'Wins', 'OBP', 'SLG', 'Team Batting Average', 'Playoffs']
data = data[selected_columns]

# Define the prediction model
# You can customize this model based on your requirements
# Here, we are using a simple rule-based model
data['Playoffs'] = 0  # Initialize all teams as not making the playoffs
data.loc[(data['Wins'] > 90) & (data['OBP'] > 0.350) & (data['SLG'] > 0.450), 'Playoffs'] = 1

# Print the prediction model
print("Prediction Model:")
print("Teams with Wins > 90, OBP > 0.350, and SLG > 0.450 will make the playoffs.")

# Print the updated DataFrame with the prediction
print("\nUpdated DataFrame:")
print(data)

# Go Yankees!