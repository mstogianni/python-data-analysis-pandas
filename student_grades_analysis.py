import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random


def mis_val(d):
    """Fill missing Age and Grade values with the column mean."""
    df = d.copy()  # work on a copy to avoid chained assignment issues

    mean_age = df['Age'].mean()
    mean_grade = df['Grade'].mean()

    df['Age'] = df['Age'].fillna(mean_age)
    df['Grade'] = df['Grade'].fillna(mean_grade)

    return df



# Create dictionary with data
data = {
    'Name': ['Nikos', 'Christos', 'Maria', 'Giorgos', 'Markos',
             'James', 'Paul', 'Kostas', 'Vasilis', 'Dimitris'],
    'Age': [20, 21, 19, 21, 21, 25, 27, 21, 30, 43],
    'Grade': [3.0, 7.0, 8.4, 3.2, 6.5, 9.0, 2.0, 2.3, 6.9, 8.0]
}

# Create DataFrame
df = pd.DataFrame(data)

print("DataFrame:\n", df)

print("\nFirst 5 rows:\n", df.head())

# Filter rows where Age > 22
df_1 = df.loc[df['Age'] > 22]
print("\nRows with Age greater than 22:\n", df_1)

# Add City column
df['City'] = 'Lamia'
print("\nOriginal DataFrame with added 'City' column:\n", df)

# Sort by Age in descending order
sorted_df = df.sort_values(by='Age', ascending=False)
print("\nDataFrame sorted by Age (descending):\n", sorted_df)

# Mean age
mean_age = df["Age"].mean()
print("\nMean age:", mean_age)

# Create a copy and concatenate
df_copy = df.copy()
con = pd.concat([df, df_copy], ignore_index=True)
print("\nConcatenated DataFrame (original + copy):\n", con)

# Save to CSV file
con.to_csv('data.csv', index=False)
print("\nSaved concatenated DataFrame to 'data.csv'\n")

# Histogram of grades per age
plt.figure(figsize=(10, 6))
for age in con['Age'].unique():
    subset = con[con['Age'] == age]
    plt.hist(subset['Grade'], bins=10, alpha=0.5, label=f'Age {age}')

plt.xlabel('Grade')
plt.ylabel('Frequency')
plt.title('Histogram of grades by age')
plt.legend(title='Age')
plt.show()

# Scatter plot of grades vs age
plt.figure(figsize=(10, 6))
plt.scatter(con['Age'], con['Grade'], alpha=0.7)
plt.xlabel('Age')
plt.ylabel('Grade')
plt.title('Scatter plot of grades by age')
plt.show()

# New dataset for missing value demonstration
data = {
    'Name': ['Nikos', 'Christos', 'Maria', 'Giorgos', 'Markos',
             'James', 'Paul', 'Kostas', 'Vasilis', 'Dimitris'],
    'Age': [20, 21, 19, 21, 21, 25, 22, 21, 30, 43],
    'Grade': [3.0, 7.0, 8.4, 3.2, 6.5, 9.0, 2.0, 2.3, 6.9, 8.0]
}
df = pd.DataFrame(data)

# Randomly choose indices to set as NaN
ran_num = random.randint(1, 9)
random_indices = np.random.choice(df.index, size=ran_num, replace=False)

df.loc[random_indices, 'Age'] = np.nan
df.loc[random_indices, 'Grade'] = np.nan
print("\nDataFrame with NaN values:\n", df)

# Fill NaN values using the mis_val function
ddf = mis_val(df)

print("\nDataFrame after replacing NaN values with column means:\n", ddf)

# Remove duplicates from concatenated DataFrame
cl_dup = con.drop_duplicates()
print("\nDataFrame after removing duplicate rows:\n", cl_dup)

# DataFrames for merge examples
data_1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Nikos', 'Maria', 'Markos', 'Kostas'],
    'Age': [19, 21, 22, 33]
})

print("\nFirst DataFrame:\n", data_1)

data_2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Grade': [9.8, 8.9, 7.5, 5.0],
    'City': ['Athens', 'Thessaloniki', 'Lamia', 'Patras']
})

print("\nSecond DataFrame:\n", data_2)

# Inner join
print("\nInner join on 'ID':\n", pd.merge(data_1, data_2, on='ID', how='inner'))

# Outer join
print("\nOuter join on 'ID':\n", pd.merge(data_1, data_2, on='ID', how='outer'))
# Outer join keeps all rows from both DataFrames,
# filling with NaN where there is no matching 'ID'

# Random numbers from random and NumPy
random_number = random.random()  # Random float between 0 and 1
print("\nRandom number from 'random' module:", random_number)

numpy_random_number = np.random.rand()  # Random float between 0 and 1
print("Random number from NumPy:", numpy_random_number)

# For small projects and simple use cases, the built-in 'random' module is usually enough.
# For larger projects, scientific computing, or big data processing,
# NumPy's random functions are faster and more efficient.
