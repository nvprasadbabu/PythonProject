# https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html
# 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

# Series
print(" ============ Series ============")
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(s)
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=['a', 'b', 'c', 'd', 'e', 'f'], name='MySeries')
print(s)
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=['a', 'b', 'c', 'd', 'e', 'f'], name='MySeries', dtype=np.float32)
print(s)
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=['a', 'b', 'c', 'd', 'e', 'f'], name='MySeries', dtype=np.float32, copy=True)
print(s)
#s = pd.Series([1, 3, 5, np.nan, 6, 8], index=['a', 'b', 'c', 'd', 'e', 'f'], name='MySeries', dtype=np.float32, copy=True, fastpath=True)
s = pd.Series(np.random.randn(6), index=['a', 'b', 'c', 'd', 'e', 'f'])
print(s)

# DataFrame
print(" ============ DataFrame ============")
dates = pd.date_range('20230101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

# DataFrame from dict of objects
print("\n ============ DataFrame from dict of objects ============")
# df2 = pd.DataFrame({'A': 1.,
#                     'B': pd.Timestamp('20230102'),
#                     'C': pd.Series(1, index=list(range(6)), dtype='float32'),
#                     'D': np.array([3] * 4, dtype='int32'),
#                     'E': pd.Categorical(['test', 'train', 'test', 'train']),
#                     'F': 'foo'})

df2 = pd.DataFrame({'column_1': [21,12,3],
                    'column_2': ['a', 'b', 'c'],
                    'column_3': [1.5, 2.5, 3.5],
                    'column_4': pd.date_range('20260101', periods=3),
                    'column_5': pd.Categorical(['Prasad', 'Anu', 'Laasya']),
                    'column_6': 'foo'})

print(df2)
print(df2.dtypes)
print(df2['column_1'])
print(df2[0:3]) 

# The following line originally attempted to slice columns using df2['A':'C'],
# but __getitem__ with a slice operates on the *row* index. Since df2 has a
# default integer index (0,1,2,3), labels 'A' through 'C' are not found and
# Pandas raises a KeyError. To select a range of **columns** by label use
# .loc with a column slice instead:
print(df2.loc[:, 'column_1':'column_4'])  # selects columns A through C

# Alternatively, explicit column selection works as well:
print(df2[['column_1', 'column_2', 'column_3']])

# selecting rows by label
print(df2.loc[0])  # selects the first row by label (which is 0 in this case)
print(df2.loc[0:2])  # selects rows from label 0 to 2 (inclusive)
print(df2.loc[0:2, 'column_1':'column_4'])  # selects rows 0 to 2 and columns 1 to 4

# selecting rows by position
print(df2.iloc[0])  # selects the first row by position
print(df2.iloc[0:3])  # selects rows 0 to 3 by position
print(df2.iloc[0:3, 0:3])  # selects rows 0 to 3 and columns 0 to 3 by position


d = {'column_1': [21,12,3],
    'column_2': ['ab','A','tyz'],
    'column_3': [1,3,6]}
df3 = pd.DataFrame(d)
print(df3)

# Adding a new column to the DataFrame by performing an operation on existing columns
df3['column_4'] = df3['column_1'] * df3['column_3']
print(df3)

# Adding a new column with a constant value
df3['column_5'] = 'constant_value'
print(df3)

# Adding a new column with values from a list
df3['column_6'] = [10, 20, 30]
print(df3)

# Adding a new column with values from a NumPy array
df3['column_7'] = np.array([100, 200, 300])
print(df3)

# Adding a new column with values from another DataFrame (using the same index)
df4 = pd.DataFrame({'column_8': [1000, 2000, 3000]}, index=df3.index)
df3['column_8'] = df4['column_8']
print(df3)

# Adding a new column with values from a function applied to existing columns
df3['column_9'] = df3['column_1'] + df3['column_3']
print(df3)

# Adding a new column with values from a lambda function applied to existing columns
df3['column_10'] = df3.apply(lambda row: row['column_1'] * row['column_3'], axis=1)
print(df3)

# Adding a new column with values from a conditional expression based on existing columns
df3['column_11'] = df3['column_1'].apply(lambda x: 'high' if x > 10 else 'low')
print(df3)

# Adding a new column with values from a map of existing column values
mapping = {21: 'twenty-one', 12: 'twelve', 3: 'three'}
df3['column_12'] = df3['column_1'].map(mapping)
print(df3)

# Adding a new column with values from a combination of existing columns using string concatenation
df3['column_13'] = df3['column_2'] + '_' + df3['column_5']
print(df3)

# deleting a column from the DataFrame
del df3['column_13']
print(df3)

df3.drop('column_12', axis=1, inplace=True) # using inplace=True to modify the DataFrame in place permanently
print(df3)

# Selecting a subset of columns from the DataFrame
subset = df3[['column_1', 'column_3', 'column_4']]
print(subset)

# Selecting rows based on a condition
filtered_rows = df3[df3['column_1'] > 10]
print(filtered_rows)

# Selecting rows based on multiple conditions
filtered_rows_multi = df3[(df3['column_1'] > 10) & (df3['column_3'] < 5)]
print(filtered_rows_multi)

# Selecting rows based on string matching
filtered_rows_string = df3[df3['column_2'].str.contains('A')]   
print(filtered_rows_string)

# Selecting rows based on missing values
filtered_rows_missing = df3[df3['column_1'].isnull()]
print(filtered_rows_missing)

# Selecting rows based on non-missing values
filtered_rows_non_missing = df3[df3['column_1'].notnull()]
print(filtered_rows_non_missing)

# Selecting rows based on the index
filtered_rows_index = df3[df3.index.isin([0, 2])]   
print(filtered_rows_index)

# Selecting rows based on the position
filtered_rows_position = df3.iloc[0:2]
print(filtered_rows_position)

print("\n\n ============ Operations ============")

df = pd.DataFrame({'col1':[1,2,3,14,25],'col2':[44,44,66,54,52],'col3':['ab','de','gc','xc','we']})
print(df)
print(df.head(3))
print(df.tail(2))
print(df.describe())    
# The describe() method generates descriptive statistics that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN values. It provides a quick overview of the data, including count, mean, standard deviation, minimum, 25th percentile (Q1), median (50th percentile or Q2), 75th percentile (Q3) and maximum values for each numeric column in the DataFrame.
# The describe() method is useful for getting a quick summary of the data and identifying any potential outliers or anomalies in the dataset. It can also be used to compare different columns in the DataFrame and identify any patterns or trends in the data.
print(df.T)  # Transpose of the DataFrame

print(df.sort_values(by='col2'))  # Sort the DataFrame by values in column 'col2'
print(df.sort_values(by='col2', ascending=False))  # Sort the DataFrame by values in column 'col2' in descending order
print(df.sort_values(by=['col2', 'col1']))  # Sort the DataFrame by values in column 'col2' and then by values in column 'col1'

print(df['col2'].sum())  # Sum of values in column 'col2'
print(df['col2'].mean())  # Mean of values in column 'col2'
print(df['col2'].std())  # Standard deviation of values in column 'col2'
print(df['col2'].min())  # Minimum value in column 'col2'
print(df['col2'].max())  # Maximum value in column 'col2'
print(df['col2'].count())  # Count of non-null values in column 'col2'
print(df['col2'].value_counts())  # Count of unique values in column 'col2'

# string operations
print(df['col3'].str.upper())  # Convert strings in column 'col3' to uppercase
print(df['col3'].str.lower())  # Convert strings in column 'col3' to lowercase
print(df['col3'].str.len())  # Get the length of strings in column 'col3'
print(df['col3'].str.contains('a'))  # Check if strings in column 'col3' contain the substring 'a'
print(df['col3'].str.replace('a', 'x'))  # Replace 'a' with 'x' in strings in column 'col3'
print(df['col3'].str.split('e'))  # Split strings in column 'col3' by the delimiter 'e'


df1 = pd.DataFrame([[np.nan, 10, np.nan, 5], [13, 44, np.nan, 11],
                    [np.nan, np.nan, np.nan, 15]],
                   columns=list('ABCD'))
print(df1)
print(df1.isnull())  # Check for NaN values
print(df1.notnull())  # Check for non-NaN values

print(df1.dropna())  # Drop rows with any NaN values
print(df1.dropna(axis=1))  # Drop columns with any NaN values
print(df1.dropna(thresh=2))  # Drop rows with less than 2 non-NaN values
print(df1.dropna(thresh=3))  # Drop rows with less than 3 non-NaN values
print(df1.fillna(0))  # Fill NaN values with 0
print(df1.ffill())  # Forward fill NaN values
print(df1.bfill())  # Backward fill NaN values

#The output will be a sparse matrix where each column corresponds to one possible value of one feature
dfhot = pd.DataFrame({'gender':['male','female','male','female','male'],'age_range':['young','adult','senior','young','adult']})
print(dfhot)

# One-hot encoding using get_dummies
df_encoded = pd.get_dummies(dfhot, columns=['gender', 'age_range'])
print(df_encoded)

data_dummies = pd.get_dummies(dfhot)
print(data_dummies)

""" # One-hot encoding using the OneHotEncoder from scikit-learn
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(sparse=False)
df_encoded_sklearn = encoder.fit_transform(dfhot[['gender', 'age_range']])
print(df_encoded_sklearn) 
"""

print("\n =================== Functions =================== \n")

df = pd.DataFrame({'col1':[1,2,3,4,5],'col2':[3,5,4,2,5],'col3':['ac','df','gi','wr','xf']})
print(df)

# Applying a function to each element in a column
df['col1_squared'] = df['col1'].apply(lambda x: x**2)
print(df)
# Applying a function to each row in the DataFrame
df['col_sum'] = df.apply(lambda row: row['col1'] + row['col2'], axis=1)
print(df)

# Applying a function to each column in the DataFrame
col_means = df.apply(lambda col: col.mean() if col.dtype in ['int64 ', 'float64'] else None)
print(col_means)

def log10(x):
    return np.log10(x)

# Applying a custom function to a column
df['col1_log10'] = df['col1'].apply(log10)
print(df)

# Applying a custom function to each row
def row_product(row):
    return row['col1'] * row['col2']   
df['col_product'] = df.apply(row_product, axis=1)
print(df)

def getsupport(X,data):
    N = len(data)
    support = (data==X).sum() / N
    return support
print(getsupport(1, df['col2']))  # Support for value 1 in column 'col2'
print(getsupport(2, df['col2']))  # Support for value 2 in column 'col2'
print(getsupport(3, df['col2']))  # Support for value 3 in column 'col2'
print(getsupport(4, df['col2']))  # Support for value 4 in column 'col2'
print(getsupport(5, df['col2']))  # Support for value 5 in column 'col2'

items = [1, 2, 3, 4, 5]

def sqrt(x): return np.sqrt(x)

# map iterator
list(map(sqrt, items))

df['col2_sqrt'] = df['col2'].map(sqrt)
print(df)

def quadratic(x): return x**2
df['col1_quadratic'] = df['col1'].map(quadratic)
print(df)

# lambda function with map iterator
df['col5'] = list(map(lambda x : x * 2, df['col1']))
print(df)

print("\n =================== Importing and exporting Data =================== \n")

df = pd.read_csv('data/Iris.csv')  # Read a CSV file into a DataFrame
print(df.head())  # Display the first few rows of the DataFrame
print(df.info())  # Display information about the DataFrame, including data types and non-null counts
print(df.tail())  # Display the last few rows of the DataFrame
print(df.describe())  # Generate descriptive statistics for the DataFrame
print(df.columns)  # Display the column names of the DataFrame
print(df.index)  # Display the index of the DataFrame
print(df['SepalLengthCm'].max())  # Get the maximum value in the 'SepalLengthCm' column
print(df['SepalLengthCm'].min())  # Get the minimum value in the 'SepalLengthCm' column
print(df['SepalLengthCm'].mean())  # Get the mean value in the 'SepalLengthCm' column
print(df['SepalLengthCm'].std())  # Get the standard deviation in the 'SepalLengthCm' column
print(df['SepalLengthCm'].value_counts())  # Get the count of unique values in the 'SepalLengthCm' column
print(df['Species'].value_counts())  # Get the count of unique values in the 'Species' column
print(df['PetalWidthCm'][0:5].sum())  # Calculate the sum of the first 5 values in the 'PetalWidthCm' column
print(df['PetalWidthCm'][0:5].cumsum())  # Calculate the cumulative sum of the first 5 values in the 'PetalWidthCm' column 

#%matplotlib inline
print(df['PetalLengthCm'].plot().set_title("First diag"))  # Plot the 'PetalLengthCm' column


df.to_csv('data/Iris_output.csv', index=False)  # Write the DataFrame to a CSV file without the index

df=pd.read_excel('data/salesdata.xls', sheet_name='Data') # Read an Excel file into a DataFrame, specifying the sheet name
print(df.head(10))

# Reading a specific sheet from an Excel file
#df_sheet2 = pd.read_excel('data/salesdata.xls', sheet_name='Sheet2')
#print(df_sheet2.head(10))

# Writing a DataFrame to an Excel file
df.to_excel('data/salesdata_output.xlsx', sheet_name='Data', index=False)

# Reading a specific range of cells from an Excel file
df_range = pd.read_excel('data/salesdata.xls', sheet_name='Data', usecols='A:C', skiprows=1, nrows=5)
print(df_range)

# Reading an Excel file with multiple sheets into a dictionary of DataFrames
dfs = pd.read_excel('data/salesdata.xls', sheet_name=None) 
print(dfs.keys())  # Print the sheet names
print(dfs['Data'].head())  # Access the DataFrame for the 'Data' sheet and display the first few rows

# Reading a table
df1 = pd.read_table('data/wind.data', sep='\s+')  # Read a table
print(df1.head())  # Display the first few rows of the DataFrame

df1 = pd.read_table('data/wind.data', header=None, sep='\s+')  # Read a table
print(df1.head())  # Display the first few rows of the DataFrame

# Read text file with comments
df = pd.read_table('data/textdata.txt', comment='#', sep=',', header=None)  # Read a text file, ignoring lines that start with '#'
print(df.head())  # Display the first few rows of the DataFrame

print("\n =================== Pandas: Merge, Join, Concat and Group by =================== \n")

data1 = {
        'id': ['1', '2', '3', '4', '5'],
        'first_name': ['Sam', 'Betty', 'Adam', 'Alice', 'Bill'], 
        'last_name': ['Hills', 'Li', 'Roberts', 'Chan', 'Howard']}
df1 = pd.DataFrame(data1, columns = ['id', 'first_name', 'last_name'])
print(df1)

data2 = {
        'id': ['3', '4', '5', '6', '7'],
        'first_name': ['Adam', 'Alice', 'Bill', 'Charlie', 'David'],
        'last_name': ['Roberts', 'Chan', 'Howard', 'Smith', 'Johnson']}
df2 = pd.DataFrame(data2, columns = ['id', 'first_name', 'last_name'])
print(df2)

data3 = {
        'id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
df3 = pd.DataFrame(data3, columns = ['id','test_id'])
print(df3)

print("# Merge df1 and df2 on the 'id' column using an inner join")
merged_df = pd.merge(df1, df2, on='id', how='inner')
print(merged_df)

# Merge df1 and df2 on the 'id' column using a left join
merged_df_left = pd.merge(df1, df2, on='id', how='left')
print(merged_df_left)

# Merge df1 and df2 on the 'id' column using a right join
merged_df_right = pd.merge(df1, df2, on='id', how='right')
print(merged_df_right)

# Merge df1 and df2 on the 'id' column using an outer join
merged_df_outer = pd.merge(df1, df2, on='id', how='outer')
print(merged_df_outer)

# Join df1 and df3 on the 'id' column using an inner join
joined_df = df1.set_index('id').join(df3.set_index('id'), how='inner')
print(joined_df)

# Join df1 and df3 on the 'id' column using a left join
joined_df_left = df1.set_index('id').join(df3.set_index('id'), how='left')
print(joined_df_left)

# Join df1 and df3 on the 'id' column using a right join
joined_df_right = df1.set_index('id').join(df3.set_index('id'), how='right')
print(joined_df_right)

# Join df1 and df3 on the 'id' column using an outer join
joined_df_outer = df1.set_index('id').join(df3.set_index('id'), how='outer')
print(joined_df_outer)

# Concatenate df1 and df2 vertically (stacking rows)
concat_df_vertical = pd.concat([df1, df2], ignore_index=True)   
print(concat_df_vertical)

# Concatenate df1 and df2 horizontally (stacking columns)
concat_df_horizontal = pd.concat([df1, df2], axis=1)    
print(concat_df_horizontal)


df = pd.DataFrame({'FactorA': [.6, .9, .3, 1.5],
                    'FactorB': [41, 43, 4, 15],
                    'FactorC': [1, 3, 2, 6],
                    'Class': ['0', '1', '1', '0']},index=[0, 1, 2, 3])
print(df)
dfrouped = df.groupby('Class')  # Group the DataFrame by the 'Class' column
print(dfrouped)  # Display the GroupBy object
print(dfrouped.sum())  # Calculate the sum of each group

# Calculate the mean of each group
group_means = dfrouped.mean()
print(group_means)  # Display the mean values for each group

# Calculate the count of each group
group_counts = dfrouped.count()
print(group_counts)  # Display the count of each group

print("\n =================== Pandas: Time Series  =================== \n")

import datetime


# working with string dates: converting string to dates
print(datetime.datetime.strptime("2018/1/1", "%Y/%m/%d"))

#converting date to text
print(datetime.datetime(2018,1,1,0,0).strftime("%Y%m%d"))

print(pd.to_datetime("15.02.2018"))
print(pd.to_datetime("12/24/2018"))
print(pd.to_datetime("07/04/2018", dayfirst=True))

# Create a date range
date_range = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
print(date_range)

# Create a time series with a date range as the index
time_series = pd.Series(np.random.randn(len(date_range)), index=date_range)
print(time_series)

#Alias	Description
#B	business day frequency
#C	custom business day frequency
#D	calendar day frequency
#W	weekly frequency
#ME	month end frequency
#SM	semi-month end frequency (15th and end of month)
#BM	business month end frequency
#CBM	custom business month end frequency
#MS	month start frequency
#SMS	semi-month start frequency (1st and 15th)
#BMS	business month start frequency
#CBMS	custom business month start frequency
#Q	quarter end frequency
#BQ	business quarter end frequency
#QS	quarter start frequency
#BQS	business quarter start frequency
#A, Y	year end frequency
#BA, BY	business year end frequency
#AS, YS	year start frequency
#BAS, BYS	business year start frequency
#BH	business hour frequency
#H	hourly frequency
#T, min	minutely frequency
#S	secondly frequency
#L, ms	milliseconds
#U, us	microseconds
#N	nanoseconds

df = pd.read_csv('data/AirPassengers.csv')
print(df.head())

# Parse the 'Month' column as datetime and use it as the index
# (pandas >= 3.0 removed the `date_parser` argument from read_csv)
df = pd.read_csv('data/AirPassengers.csv', parse_dates=['Month'], index_col='Month')
print(df.head())

#Specify the entire range:
print(df['1960-01-01':'1960-12-01'])

#Use ':' if one of the indices is at ends:
print(df['1960-06-01':])

ax = df.plot().set_title("Air Passengers Over Time")  # Set the title of the plot
plt.show()
