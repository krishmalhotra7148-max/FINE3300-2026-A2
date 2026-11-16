# FINE 3300 - Assignment 2, Part B: Inflation Calculator

import numpy as np
import pandas as pd

# 1. Load the data (same as the graph file)
data_frame = pd.read_csv('cpi.csv', skiprows=8)
data_frame = data_frame.rename(columns={'date': 'Date', 'STATIC_INFLATIONCALC': 'CPI'})
data_frame['Date'] = pd.to_datetime(data_frame['Date'])

# 2. Annual CPI (average of the 12 months in each year)


data_frame['Year'] = data_frame['Date'].dt.year
annual_cpi = data_frame.groupby('Year')['CPI'].apply(np.mean)

first_year = annual_cpi.index.min()
last_year = annual_cpi.index.max()

# 3. Functions that keep asking until the user gives a valid value
def get_price():
    while True:
        text = input('Enter the price: $').replace(',', '').replace('$', '')
        try:
            price = float(text)
        except ValueError:
            print('  Please enter a number, e.g. 100 or 1,250.50')
            continue
        if price <= 0:
            print('  The price must be greater than 0.')
            continue
        return price


def get_year(prompt):
    while True:
        text = input(prompt).strip()
        try:
            year = int(text)
        except ValueError:
            print('  Please enter a year as a whole number, e.g. 2000')
            continue
        if year < first_year or year > last_year:
            print(f'  The data only covers {first_year} to {last_year}.')
            continue
        return year


# 4. Get inputs from the user
print(f'Inflation Calculator (CPI data from {first_year} to {last_year})')
price = get_price()
year1 = get_year('Enter the starting year: ')
year2 = get_year('Enter the ending year: ')

# 5. Look up CPI for each year
cpi1 = annual_cpi.loc[year1]
cpi2 = annual_cpi.loc[year2]

# 6. Calculations
new_price = price * cpi2 / cpi1
pct_change = (cpi2 / cpi1 - 1) * 100
n_years = abs(year2 - year1)

# The annual rate is the constant yearly rate that gives the same total change.
# It is 0 when both years are the same (nothing to annualize).
if n_years == 0:
    annual_rate = 0.0
else:
    annual_rate = (np.power(cpi2 / cpi1, 1 / (year2 - year1)) - 1) * 100

# 7. Results
print(50 * '-')
print(f'${price:,.2f} CAD in {year1} = ${new_price:,.2f} CAD in {year2}')
print(50 * '-')
print(f'Percent change:        {pct_change:,.2f}%')
print(f'Number of years:       {n_years}')
print(f'Annual rate of change: {annual_rate:.2f}%')
print(f'CPI in {year1}:           {cpi1:.1f}')
print(f'CPI in {year2}:           {cpi2:.1f}')