import pandas as pd
import numpy as np

## Binomial Distribution (It's like flipping a coin "50/50")

x = np.random.binomial(1000, 0.5) / 1000
y = np.random.binomial(20, .5, 10000)

print (y>=15).mean()

chance_of_tornado = 0.01 / 100
z = np.random.binomial(10000, chance_of_tornado)

print z

"""
Situation: probability of a tornado: 1%
Question: how is the chance of it happens two days in a row
"""

chance_of_tornado = 0.01

tornado_events = np.random.binomial(1, chance_of_tornado, 1000000)

two_days_in_a_row = 0
for j in range(1, len(tornado_events)-1):
	if tornado_events[j]==1 and tornado_events[j-1] == 1:
		two_days_in_a_row+=1

print '{} tornadoes back to back in {} years.'.format(two_days_in_a_row, 1000000/365)