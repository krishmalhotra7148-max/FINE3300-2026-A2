# FINE 3300 - Assignment 2, Part B: Inflation Calculator

import pandas as pd

# 1. Load the data (same as the graph file)
data_frame = pd.read_csv('cpi.csv.csv', skiprows=8)
data_frame = data_frame.rename(columns={'date': 'Date', 'STATIC_INFLATIONCALC': 'CPI'})
data_frame['Date'] = pd.to_datetime(data_frame['Date'])

# 2. Annual CPI (average of the 12 months in each year)
data_frame['Date'] = pd.to_datetime(data_frame['Date'])

data_frame['Annual Pct Change'] = data_frame['CPI'].pct_change(periods=12) * 100
data_frame['Annual Pct Change'] = data_frame['Annual Pct Change'].round(2)

data_frame['Year'] = data_frame['Date'].dt.year
annual_cpi = data_frame.groupby('Year')['CPI'].mean()

# 3. Get inputs from the user
price = float(input('Enter the price: $'))
year1 = int(input('Enter the starting year: '))
year2 = int(input('Enter the ending year: '))

# 4. Look up CPI for each year
cpi1 = annual_cpi.loc[year1]
cpi2 = annual_cpi.loc[year2]

# 5. Calculations
new_price = price * cpi2 / cpi1
pct_change = (cpi2 / cpi1 - 1) * 100
n_years = year2 - year1
annual_rate = ((cpi2 / cpi1) ** (1 / n_years) - 1) * 100

# 6. Results
print(50 * '-')
print(f'${price:,.2f} in {year1} is worth ${new_price:,.2f} in {year2}')
print(f'Percent change:{pct_change:.2f}%')
print(f'Number of years:{n_years}')
print(f'Annual rate of change: {annual_rate:.2f}%')
print(f'CPI in {year1}:{cpi1:.1f}')
print(f'CPI in {year2}:{cpi2:.1f}')