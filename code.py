
import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
production_data = pd.read_csv("C:\\Users\\ishik\\Downloads\\Renewable energy Production share of primary energy - World, 1900-2016 (in %).csv")
consumption_data = pd.read_csv("C:\\Users\\ishik\\Downloads\\Renewable energy Consumption share of primary energy - World, 1980-2016 (in %).csv")

# Data Cleaning and Renaming
production_data = production_data.rename(columns={'Unnamed: 0': 'Year', 'World': 'Renewable Energy Production Share (%)'})
consumption_data = consumption_data.rename(columns={'Unnamed: 0': 'Year', 'World': 'Renewable Energy Consumption Share (%)'})

# Extract just the year from the "Year" column and convert to integer
production_data['Year'] = pd.to_datetime(production_data['Year']).dt.year
consumption_data['Year'] = pd.to_datetime(consumption_data['Year']).dt.year

# Verify the cleaned datasets
print("Production Data Overview:")
print(production_data.head())
print("\nConsumption Data Overview:")
print(consumption_data.head())

# Check for missing values
print("\nMissing Values in Production Data:")
print(production_data.isnull().sum())

print("\nMissing Values in Consumption Data:")
print(consumption_data.isnull().sum())

# Descriptive statistics for each dataset
print("\nProduction Data Statistics:")
print(production_data.describe())

print("\nConsumption Data Statistics:")
print(consumption_data.describe())

# Visualize Renewable Energy Production over the years
plt.figure(figsize=(10, 5))
plt.plot(production_data['Year'], production_data['Renewable Energy Production Share (%)'], marker='o', color='b', label='Production Share (%)')
plt.title('Renewable Energy Production Share Over Time')
plt.xlabel('Year')
plt.ylabel('Production Share (%)')
plt.grid(True)
plt.legend()
plt.show()

# Visualize Renewable Energy Consumption over the years
plt.figure(figsize=(10, 5))
plt.plot(consumption_data['Year'], consumption_data['Renewable Energy Consumption Share (%)'], marker='o', color='r', label='Consumption Share (%)')
plt.title('Renewable Energy Consumption Share Over Time')
plt.xlabel('Year')
plt.ylabel('Consumption Share (%)')
plt.grid(True)
plt.legend()
plt.show()

# Comparing Production and Consumption trends
plt.figure(figsize=(12, 6))
plt.plot(production_data['Year'], production_data['Renewable Energy Production Share (%)'], marker='o', color='b', label='Production Share (%)')
plt.plot(consumption_data['Year'], consumption_data['Renewable Energy Consumption Share (%)'], marker='s', color='r', label='Consumption Share (%)')
plt.title('Renewable Energy Production vs. Consumption Share Over Time')
plt.xlabel('Year')
plt.ylabel('Share (%)')
plt.grid(True)
plt.legend()
plt.show()
