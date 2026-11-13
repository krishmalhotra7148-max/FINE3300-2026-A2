# FINE 3300 - Assignment 2, Part B: Consumer Price Index

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 1. Load the data
# The Bank of Canada CSV has 8 lines of info text at the top
data_frame = pd.read_csv('cpi.csv.csv', skiprows=8)

data_frame = data_frame.rename(columns={'date': 'Date', 'STATIC_INFLATIONCALC': 'CPI'})

# Convert dates from text to real dates, then pull out the year
data_frame['Date'] = pd.to_datetime(data_frame['Date'])

data_frame['Annual Pct Change'] = data_frame['CPI'].pct_change(periods=12) * 100
data_frame['Annual Pct Change'] = data_frame['Annual Pct Change'].round(2)

print(data_frame.tail(5))

import matplotlib.pyplot as plt
plt.plot(data_frame['Date'], data_frame['CPI'])
plt.show()
