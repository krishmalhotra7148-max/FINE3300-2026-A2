# FINE 3300 - Assignment 2, Part B: Inflation Calculator

import numpy as np
import pandas as pd

# 1. Load the data (same as the graph file)
data_frame = pd.read_csv('cpi.csv', skiprows=8)
data_frame = data_frame.rename(columns={'date': 'Date', 'STATIC_INFLATIONCALC': 'CPI'})
data_frame['Date'] = pd.to_datetime(data_frame['Date'])

# Use the date as the index so a CPI value can be looked up by date
monthly_cpi = data_frame.set_index('Date')['CPI']

first_date = monthly_cpi.index.min()
last_date = monthly_cpi.index.max()

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

def get_date(prompt):
    while True:
        text = input(prompt).strip()

        # Validate the format: must be a year and a month, e.g. 2020-03
        try:
            date = pd.to_datetime(text, format='%Y-%m')
        except ValueError:
            print('  Please use the format YYYY-MM, e.g. 2020-03')
            continue

        # Make sure the date is inside the data set
        if date < first_date or date > last_date:
            print(f'  The data only covers {first_date:%Y-%m} to {last_date:%Y-%m}.')
            continue
        return date


# 3. Get inputs from the user
print(f'Enhanced Inflation Calculator (monthly CPI, {first_date:%B %Y} to {last_date:%B %Y})')
price = get_price()
date1 = get_date('Enter the first date (YYYY-MM): ')
date2 = get_date('Enter the second date (YYYY-MM): ')

# 4. Extract the month and year from each date
year1, month1 = date1.year, date1.month
year2, month2 = date2.year, date2.month

# 5. Look up the CPI for each month
cpi1 = monthly_cpi.loc[date1]
cpi2 = monthly_cpi.loc[date2]

# 6. Calculations
new_price = price * cpi2 / cpi1
pct_change = (cpi2 / cpi1 - 1) * 100

# Number of years between the two dates (months count as a fraction of a year)
n_months = (year2 - year1) * 12 + (month2 - month1)
n_years = n_months / 12

# The annual rate is the constant yearly rate that gives the same total change.
# It is 0 when both dates are the same (nothing to annualize).
if n_months == 0:
    annual_rate = 0.0
else:
    annual_rate = (np.power(cpi2 / cpi1, 1 / n_years) - 1) * 100

# 7. Results
label1 = f'{date1:%B %Y}'
label2 = f'{date2:%B %Y}'

print(50 * '-')
print(f'${price:,.2f} CAD in {label1} = ${new_price:,.2f} CAD in {label2}')
print(50 * '-')
print(f'Percent change:        {pct_change:,.2f}%')
print(f'Number of years:       {np.abs(n_years):.2f}')
print(f'Annual rate of change: {annual_rate:.2f}%')
print(f'CPI in {label1}: {cpi1:.1f}')
print(f'CPI in {label2}: {cpi2:.1f}')