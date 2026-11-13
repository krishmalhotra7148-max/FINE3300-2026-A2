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

fig, ax = plt.subplots(figsize=(10, 5), layout='constrained')

ax.plot(data_frame['Date'], data_frame['CPI'], color='blue', label='CPI')

ax.set_xlabel('Date')
ax.set_ylabel('CPI (2002 = 100)')
ax.set_title('Consumer Price Index (CPI) Over Time')

# Add a horizontal line at CPI = 100
ax.axhline(y=100, linestyle=':', color='gray', label='Base level (2002 = 100)')

# Add a second y-axis for the annual percentage change
ax2 = ax.twinx()
ax2.plot(data_frame['Date'], data_frame['Annual Pct Change'], color='orange', label='Annual Percentage Change (%)', linewidth=0.8)
ax2.set_ylabel('Annual Percentage Change (%)')

lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc='lower right')
fig.savefig('cpi_graph.png')
plt.show()