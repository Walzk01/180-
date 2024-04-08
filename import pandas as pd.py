# Import the necessary libraries
import pandas as pd

# Define the file path of the spreadsheet
file_path = (r'C:\Users\walzk01\Downloads\Restaurant Revenue.xlsx')

# Read the spreadsheet into a pandas DataFrame
df = pd.read_excel(file_path)

# Select the required columns: Number_of_Customers, Menu_Price, Marketing_Spend, Promotions, Reviews, Monthly_Revenue
selected_columns = ['Number_of_Customers', 'Menu_Price', 'Marketing_Spend', 'Promotions', 'Reviews', 'Monthly_Revenue']
df_selected = df[selected_columns]

# Create a new column 'Average_Customer_Spending' by dividing 'Menu_Price' by 'Number_of_Customers'
df_selected['Average_Customer_Spending'] = df_selected['Menu_Price'] / df_selected['Number_of_Customers']

# Create a new DataFrame 'table_model' with columns 'Average_Customer_Spending' and 'Monthly_Revenue'
table_model = df_selected[['Average_Customer_Spending', 'Monthly_Revenue']]

# Print the table model
print(table_model)

#Go Yankees!