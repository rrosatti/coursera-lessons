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

#df3 = df3.apply(lambda x: np.max(x[rows]), axis=1)
#print(df3)


## ------------------------------- Group By ------------------------

## calculate the avg pop by state
"""for group, frame in df3.groupby('STNAME'):
	avg = np.average(frame['CENSUS2010POP'])
	print('Counties in state ' + group + ' have an average population of ' + str(avg))
"""

## another cool way to do the same thing
#print(df3.groupby('STNAME').agg({'CENSUS2010POP': np.average}))

## Group by "Series"
#print(df3.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average, 'sum': np.sum}))

## Group by "DataFrame"
"""print(df3.set_index('STNAME').groupby(level=0)['POPESTIMATE2010', 'POPESTIMATE2011']
	.agg({'avg': np.average, 'sum': np.sum}))
"""

## ------------------------------- Scales ------------------------

"""
Ratio Scale:  units are equally spaced (Ex: weight, height)
Interval Scale: units are equally spaced, but there is no true zero
Ordinal Scale: the order of the units are important, but not evenly spaced (Ex: Letter grades A+, A)
Nominal Scale: categories of data, but the categories have no order with respect to one another (Ex: Teams of a sport)
	- In pandas it is called Categorical data
"""

df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
df.rename(columns={0: 'Grades'}, inplace=True)

## create a category
grades = df['Grades'].astype('category', 
							categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
							ordered=True)

print(grades)

print(grades > 'B')

## using cut function
## Ex: cut could convert ages to groups of age ranges.
s = pd.Series([19, 21, 45, 78, 46, 24, 39, 68, 62, 29])
print(pd.cut(s, 3, labels=['Young', 'Adult', 'Elder']))


## ------------------------------- Pivot Tables ------------------------
## Pivot Tables are used to reorganize and summarize selected columns and rows of data in order to obtain a desired report.[DataFrame]
cars_df = pd.read_csv('cars.csv')
#print(cars_df)

print(cars_df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=np.mean))

## now passing multiple functions
print(cars_df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=[np.mean, np.min], margins=True))

## ------------------------------- Date Functionality ------------------------

## Timestamp
#print(pd.Timestamp('05/12/2016 01:03PM'))

## Period
#print(pd.Period('12/2016'))
#print(pd.Period('05/12/2016'))

print
## DateTimeIndex
t1 = pd.Series(list('abc'), [pd.Timestamp('2016-12-04'), pd.Timestamp('2016-12-05'), pd.Timestamp('2016-12-06')])
print(t1)

## PeriodIndex
t2 = pd.Series(list('def'), [pd.Period('2016-11'), pd.Period('2016-12'), pd.Period('2017-01')])
print(t2)

## Converting to DateTime
d1 = ['11 June 1995', 'Jun 29, 2010', '2012-12-21', '9/15/18']
print(pd.to_datetime(d1))
print(pd.to_datetime(d1, dayfirst=True))

## TimeDeltas (Difference in Time)
print(pd.Timestamp('05-12-2016 1:15PM') + pd.Timedelta('12D 12H'))

## Dates in DataFrame
	## creating range
dates = pd.date_range('01-01-2017', periods=12, freq='2W-SUN')
print dates

df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5, 10, 12).cumsum(),
                  'Count 2': 120 + np.random.randint(-5, 10, 12)}, index=dates)
print df
print df.index.weekday_name

# "group" by month(M)
print df.resample('M').mean()
# "group" by year/month
print df['2017-03']