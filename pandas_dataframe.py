import pandas as pd
import numpy as np
"""
purchase1 = pd.Series({'Name': 'Chris', 'Item Purchased': 'Dog Food', 'Cost': 22.50})
purchase2 = pd.Series({'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50})
purchase3 = pd.Series({'Name': 'Vinod', 'Item Purchased': 'Bird Seed', 'Cost': 5.00})

df = pd.DataFrame([purchase1, purchase2, purchase3], index=['Store 1', 'Store 1', 'Store 2'])
print df

print df.loc['Store 1']

print df['Cost']

print df.loc['Store 1', 'Cost']

print df.loc[:, ['Name', 'Cost']]

df.drop('Store 1') ## it does not drop the content in the dataframe
print df

del df['Name'] ## this one does
print df

df['Location'] = 'New Location' ## adding new column with 'default' values
print df
"""

## reading data from csv file
df2 = pd.read_csv('olympics.csv')
print df2

print df2.columns

## ------------------------------- Quering Data Frames ------------------------

print df2['Gold medals'] > 0 ## show the 'Boolean Mask' regarding whether 'Gold Medals' > 0 or not

only_gold = df2.where(df2['Gold medals'] > 0) ## show only the rows where 'Gold Medals' > 0
print only_gold 
print only_gold['Gold medals'].count()
print only_gold.dropna() ## shows only the rows where there is no NaN value
print only_gold['Bronze medals'].unique() ## show the unique values related to 'Bronze medals' column


## ------------------------------- Merging Data Frames ------------------------

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')

student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')

print(staff_df.head())
print()
print(student_df.head())

## using outer join
print(pd.merge(staff_df, student_df, how="outer", left_index=True, right_index=True))

## using inner join
print(pd.merge(staff_df, student_df, how="inner", left_index=True, right_index=True))

## using column instead of index
staff_df = staff_df.reset_index('Name')
student_df = student_df.reset_index('Name')
print(pd.merge(staff_df, student_df, how="left", left_on='Name', right_on='Name'))

## ------------------------------- Idiomatic Pandas: Making Code Pandorable ------------------------
## ------------------------ Idiomatic Solution: High Performance and High Readbility ---------------

## Method chaining
df3 = pd.read_csv('census.csv')
(df3.where(df3['SUMLEV'] == 50)
	.dropna()
	.set_index(['STNAME', 'CTYNAME'])
	.rename(columns={'ESTIMATEBASE2010' : "Estimates Base 2010"}))

## apply function
def min_max(row):
	data = row[['POPESTIMATE2010',
			'POPESTIMATE2011',
			'POPESTIMATE2011',
			'POPESTIMATE2012', 
			'POPESTIMATE2013', 
			'POPESTIMATE2014', 
			'POPESTIMATE2015']]
	return pd.Series({'min': np.min(data), 'max': np.max(data)})

#df3 = df3.apply(min_max, axis=1)
#print(df3)

## adding new columns to the data frame
def min_max_2(row):
	data = row[['POPESTIMATE2010',
			'POPESTIMATE2011',
			'POPESTIMATE2011',
			'POPESTIMATE2012', 
			'POPESTIMATE2013', 
			'POPESTIMATE2014', 
			'POPESTIMATE2015']]
	row['max'] = np.max(data)
	row['min'] = np.min(data)
	return row

##df3 = df3.apply(min_max_2, axis=1)
##print(df3)

## adding max column using lambda
rows = ['POPESTIMATE2010',
		'POPESTIMATE2011',
		'POPESTIMATE2011',
		'POPESTIMATE2012', 
		'POPESTIMATE2013', 
		'POPESTIMATE2014', 
		'POPESTIMATE2015']

df3 = df3.apply(lambda x: np.max(x[rows]), axis=1)
print(df3)
