import pandas as pd

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

## reading data from csv file
df2 = pd.read_csv('olympics.csv')
print df2

print df2.columns