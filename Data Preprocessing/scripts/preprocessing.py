import pandas as pd

# Read the data from the Excel file
data = pd.read_excel('../data/raw/simulated_data.xlsx')

# Preprocess the age column
data['Age'] = pd.to_datetime(data['Date of Birth']).apply(lambda x: (pd.Timestamp.now() - x).days // 365.25)  # Calculate age from Date of Birth
data['Age'] = data['Age'].fillna(data['Age'].mean())  # Replace missing values with the mean

# Preprocess the currentSG column
data['CurrentSG'] = data['Current SG'].fillna(0)  # Replace missing values with 0

# Preprocess the income column
data['Income'] = data['Income'].fillna(0).apply(lambda x: str(x).replace('$', '').replace(',', '')).astype(float)

# Preprocess the super balance column
data['Super Balance'] = data['Super Balance'].fillna(data['Super Balance'].median())  # Replace missing values with the median

# Preprocess the risk profile column
data['Risk Profile'] = data['Risk Profile'].map({'Low': 1, 'Medium': 2, 'High': 3})  # Map categorical values to numerical values

# Save the preprocessed data to a new file
#data.to_csv('/path/to/preprocessed_data.csv', index=False)
data.head()