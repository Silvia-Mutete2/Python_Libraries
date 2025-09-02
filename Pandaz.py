import pandas as pd  # We give the elder a short, respectful nickname 'pd'

# The scribe creates a table from a dictionary
data = {'Name': ['Lebo', 'Thando', 'Sipho'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Display the beautiful table
print(df)

# Calculate the average age of the village
print(f"\nThe average age is: {df['Age'].mean()} winters")