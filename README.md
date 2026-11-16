# Inflation Analysis & Calculator

**FINE 3300 — Python for Finance Professionals | Assignment 2, Part B**

This project analyzes historical Canadian inflation using monthly Consumer Price Index (CPI) data and builds an interactive Python inflation calculator. It combines data analysis, visualization, and practical calculations to show how the purchasing power of money changes over time.

The analysis uses monthly Canadian CPI data from **January 1914 to September 2026**, downloaded from the Bank of Canada and originally collected by Statistics Canada.

## Project Overview

The repository contains two Python programs:

1. **CPI Visualization (`cpi_graph.py`)**
   Reads the historical CPI data, calculates year-over-year inflation, and graphs the CPI and the inflation rate together.

2. **Enhanced Inflation Calculator (`InflationCalculator.py`)**
   The [Bank of Canada Inflation Calculator](https://www.bankofcanada.ca/rates/related/inflation-calculator/) only accepts a **year** as input, even though the CPI is published **monthly**. This calculator takes a **month and year** for each period, so it uses the exact monthly CPI values. It converts a dollar amount between the two dates and reports the cumulative and annualized change, the same results the Bank of Canada calculator shows.

## Repository Structure

| File | Description |
|------|-------------|
| `cpi.csv` | Monthly Canadian Total CPI data (Bank of Canada, CSV format) |
| `cpi_graph.py` | Loads the data, calculates annual inflation, and creates the graph |
| `cpi_graph.png` | The graph saved by `cpi_graph.py` |
| `InflationCalculator.py` | Interactive month-and-year inflation calculator |
| `README.md` | Project write-up and instructions |

## Getting Started

### Requirements

Python 3 with the following libraries:

- pandas
- NumPy
- Matplotlib

Install them with:

```bash
python -m pip install pandas numpy matplotlib
```

### Clone the Repository

```bash
git clone https://github.com/krishmalhotra7148-max/FINE3300-2026-A2.git
cd FINE3300-2026-A2
```

### Run the CPI Visualization

```bash
python cpi_graph.py
```

This program:
- Loads the CPI dataset into a pandas data frame.
- Calculates year-over-year inflation for every month.
- Plots the CPI (left axis) and the annual inflation rate (right axis), with a dotted line at the base level.
- Saves the figure as `cpi_graph.png`.

### Run the Inflation Calculator

```bash
python InflationCalculator.py
```

The calculator asks for a dollar amount and two dates in `YYYY-MM` format.

Run both programs from inside the repository folder so they can find `cpi.csv`.

---

## Part 1: Historical Canadian CPI Analysis

### CPI Visualization

![Canadian CPI and Annual Inflation Rate](cpi_graph.png)

The graph shows two measures:

- **Consumer Price Index (blue line, left axis):** the price level of the CPI basket, indexed so that **2002 = 100**. The dotted gray line marks this base level.
- **Year-over-year inflation rate (orange line, right axis):** the percentage change in the CPI compared with the same month one year earlier (formula under [Formulas](#formulas)).

Two vertical axes are used because the CPI level and the inflation rate have different units and scales.

### Commentary

- **Prices were almost flat for 50 years, then took off.** The CPI started at 6.0 in 1914 and reached 170.0 in September 2026, but most of that increase happened after 1970, where the blue line gets steep. It crosses the dotted base line in 2002, the base year.
- **The most volatile period came right after World War I.** Inflation peaked at **21.6% in June 1920**, followed by the largest price drop in the data, **-17.8% in mid-1921**. Prices fell again during the Great Depression in the early 1930s, the other stretch where the orange line goes well below zero.
- **Inflation spiked again after World War II**, reaching **17.5% in February 1948**.
- **The 1970s and early 1980s were the longest period of high inflation.** The annual rate averaged about **7.8% from 1970 to 1984** and peaked at **12.9% in July 1981**.
- **From 1992 to 2020 inflation was low and stable**, averaging about **1.8% a year**, close to the Bank of Canada's 2% target. The only negative reading in that period was **-0.9% in July 2009**, after the financial crisis.
- **The post-pandemic surge stands out.** Inflation hit **8.1% in June 2022**, the highest since the early 1980s. The latest reading in the data is **3.1% (September 2026)**.

---

## Part 2: Enhanced Inflation Calculator

### Purpose

The calculator compares the purchasing power of Canadian dollars between two specific months. Instead of averaging a whole year, as the Bank of Canada calculator does, it uses the monthly CPI value for each date, which gives a more precise comparison.

### Features

- Accepts any positive dollar amount (commas and a `$` sign are allowed).
- Takes each date in `YYYY-MM` format and extracts the month and year.
- Works for any month from January 1914 to September 2026.
- Calculates the inflation-adjusted price, the cumulative percentage change, the number of years, and the annual rate of change.
- Shows the CPI value for both dates.
- Validates every input and asks again instead of crashing.
- Works in both directions: the later date can be entered first to see what a price was worth in the past.

### Formulas

| Result | Formula |
|---|---|
| New price | price × (CPI₂ ÷ CPI₁) |
| Percent change | (new price − price) ÷ price × 100 |
| Number of months | (year₂ − year₁) × 12 + (month₂ − month₁) |
| Number of years | months ÷ 12 |
| Annual rate of change | ((CPI₂ ÷ CPI₁)^(1 ÷ years) − 1) × 100 |
| Year-over-year inflation (graph) | (CPIₜ ÷ CPIₜ₋₁₂ − 1) × 100 |

CPI₁ and CPI₂ are the CPI in the first and second month. If both dates are the same, the annual rate is 0%.

### Sample Output

**$100 in March 2000, compared with September 2026:**

```text
Enhanced Inflation Calculator (monthly CPI, January 1914 to September 2026)
Enter the price: $100
Enter the first date (YYYY-MM): 2000-03
Enter the second date (YYYY-MM): 2026-09
--------------------------------------------------
$100.00 CAD in March 2000 = $179.32 CAD in September 2026
--------------------------------------------------
Percent change:        79.32%
Number of years:       26.50
Annual rate of change: 2.23%
CPI in March 2000: 94.8
CPI in September 2026: 170.0
```

A basket of goods and services that cost **$100.00 in March 2000** would cost about **$179.32 in September 2026** if its price moved with the national CPI. That is **79.32%** cumulative growth, or about **2.23% a year**.

**Going backward: $2,500 in June 2022, compared with January 1980:**

```text
Enhanced Inflation Calculator (monthly CPI, January 1914 to September 2026)
Enter the price: $2,500
Enter the first date (YYYY-MM): 2022-06
Enter the second date (YYYY-MM): 1980-01
--------------------------------------------------
$2,500.00 CAD in June 2022 = $683.45 CAD in January 1980
--------------------------------------------------
Percent change:        -72.66%
Number of years:       42.42
Annual rate of change: 3.10%
CPI in June 2022: 152.9
CPI in January 1980: 41.8
```

### Input Validation

The program checks that:

1. The price is a number greater than 0.
2. Each date follows the `YYYY-MM` format with a real month (1 to 12).
3. Both dates fall inside the dataset (January 1914 to September 2026).

If an input fails a check, the program explains why and asks again:

```text
Enter the price: $abc
  Please enter a number, e.g. 100 or 1,250.50
Enter the price: $100
Enter the first date (YYYY-MM): March 2020
  Please use the format YYYY-MM, e.g. 2020-03
Enter the first date (YYYY-MM): 1913-12
  The data only covers 1914-01 to 2026-09.
Enter the first date (YYYY-MM): 2020-03
```

---

## Data Source

- **Source:** [Bank of Canada — Inflation Calculator](https://www.bankofcanada.ca/rates/related/inflation-calculator/) (CSV download)
- **Original data provider:** Statistics Canada, Consumer Price Indexes for Canada, Monthly
- **Series:** Total CPI, monthly
- **Base year:** 2002 = 100
- **Period covered:** January 1914 – September 2026

### Data Processing

The CSV starts with 8 lines of terms and series information, which are skipped when the file is read:

```python
data_frame = pd.read_csv('cpi.csv', skiprows=8)
```

Annual inflation is calculated as a 12-month percentage change, comparing each month with the same month one year earlier:

```python
data_frame['Annual Pct Change'] = data_frame['CPI'].pct_change(periods=12) * 100
```

To use newer data, download the latest CSV from the Bank of Canada Inflation Calculator page and save it as `cpi.csv`.

---

## Conclusion

The CPI graph shows that Canadian inflation has come in distinct episodes (the two world wars, the 1970s, and the post-pandemic surge) separated by long stable periods, and that most of the rise in prices since 1914 happened in the last 50 years. The enhanced calculator turns that history into a practical tool: by working with monthly instead of annual CPI, it measures changes in purchasing power between any two months in the dataset.

---

**Course:** FINE 3300 — Python for Finance Professionals
**Assignment:** Assignment 2, Part B
**Author:** Krish Malhotra