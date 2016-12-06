import numpy as np
import pandas as pd

sports = {'Archery': 'Bhutan', 'Golf': 'Scotland', 'Sumo': 'Japan', 'Taekwondo': 'South Korea'}
s = pd.Series(sports)
print sports

print s.iloc[3] # uses the index as a number (0, 1, 2 ...)
print s.loc['Golf']


numbers = pd.Series([100.00, 120.00, 101.00, 3.00])
## instead of doing this:
total = 0
for n in numbers:
	total+=n
print(total)

## do this:
total = np.sum(numbers)
print(total)

numbers += 2 ## adds two to each item in numbers using broadcasting
print(numbers)