import pandas as pd  # We give the elder a short, respectful nickname 'pd'

# The scribe creates a table from a dictionary
data = {'Name': ['Lebo', 'Thando', 'Sipho'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Display the beautiful table
print(df)

# Calculate the average age of the village
print(f"\nThe average age is: {df['Age'].mean()} winters")

# Add a new column for occupation
df['Occupation'] = ['Farmer', 'Blacksmith', 'Doctor']
print("\nUpdated Table with Occupation:")
print(df)

# Filter the adults older than 28 
adults = df[df['Age'] > 28]
print("\nAdults older than 28:")
print(adults)

#Sort the table by age
sorted_df = df.sort_values(by='Age')
print("\nTable sorted by Age:")
print(sorted_df)

# Save the table to a CSV file for future generations
df.to_csv('village_data.csv', index=False)
print("\nData saved to village_data.csv")