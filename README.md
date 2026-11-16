
# Inflation Analysis & Calculator

**FINE 3300 — Python for Finance Professionals | Assignment 2, Part B**

This project analyzes historical Canadian inflation using monthly Consumer Price Index (CPI) data and develops an interactive Python inflation calculator. It combines financial data analysis, visualization, and practical calculations to illustrate how the purchasing power of money changes over time.

The analysis uses monthly Canadian CPI data from **January 1914 to September 2026**, sourced from the Bank of Canada and originally collected by Statistics Canada.

## Project Overview

The repository contains two Python programs:

1. **CPI Visualization (`cpi_graph.py`)**  
   Analyzes historical CPI data, calculates year-over-year inflation rates, and visualizes changes in Canadian consumer prices.

2. **Enhanced Inflation Calculator (`InflationCalculator.py`)**  
   An interactive calculator that converts monetary amounts between two selected months using historical CPI values. It also calculates cumulative inflation and annualized rates of change.

## Repository Structure

| File | Description |
|------|-------------|
| `cpi.csv` | Historical monthly Canadian CPI dataset |
| `cpi_graph.py` | Python script for CPI analysis and visualization |
| `cpi_graph.png` | Generated CPI and inflation chart |
| `InflationCalculator.py` | Interactive monthly inflation calculator |
| `README.md` | Project documentation and instructions |

## Getting Started

### Requirements

Ensure Python 3 is installed along with the following libraries:

- pandas
- NumPy
- Matplotlib

Install the required packages using:

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
- Loads the historical CPI dataset.
- Calculates year-over-year inflation.
- Produces a dual-axis visualization.
- Saves the resulting figure as `cpi_graph.png`.

### Run the Inflation Calculator

```bash
python InflationCalculator.py
```

The calculator prompts users to enter a monetary amount and two dates in `YYYY-MM` format.

Run both programs from the repository folder so they can access `cpi.csv`.

---

## Part 1: Historical Canadian CPI Analysis

### CPI Visualization

![Canadian CPI and Annual Inflation Rate](cpi_graph.png)

The visualization displays two measures of Canadian inflation:

**Consumer Price Index (CPI)**

The blue line represents the CPI level, indexed to a base of **2002 = 100**.

**Year-over-Year Inflation Rate**

The orange line represents the percentage change in CPI relative to the same month of the previous year.

Annual inflation is calculated as:

\[
\text{Inflation Rate}_t =
\left(\frac{CPI_t}{CPI_{t-12}}-1\right)\times100
\]

The chart uses two vertical axes because the CPI level and the annual inflation rate have different units and scales.

---

## Part 2: Enhanced Inflation Calculator

### Purpose

The Enhanced Inflation Calculator allows users to compare the purchasing power of Canadian dollars between two specific months.

Rather than restricting comparisons to entire years, the program uses monthly CPI observations to provide more precise historical comparisons.

### Calculator Features

- Accepts any positive monetary amount.
- Supports monthly dates in `YYYY-MM` format.
- Allows comparisons between January 1914 and September 2026.
- Calculates the CPI-adjusted equivalent price.
- Reports the cumulative percentage change.
- Calculates the annualized rate of price change.
- Validates user inputs and handles invalid entries.
- Supports both forward and backward date comparisons.

### Methodology

The calculator uses the CPI ratio between two periods to determine the equivalent monetary value.

**Equivalent Price**

\[
P_2=P_1\times\frac{CPI_2}{CPI_1}
\]

Where:

- \(P_1\) = Original monetary amount
- \(P_2\) = Inflation-adjusted monetary amount
- \(CPI_1\) = CPI in the starting month
- \(CPI_2\) = CPI in the comparison month

**Cumulative Percentage Change**

\[
\%\text{ Change}=
\left(\frac{CPI_2}{CPI_1}-1\right)\times100
\]

**Annualized Rate of Change**

\[
r=\left[
\left(\frac{CPI_2}{CPI_1}\right)^{1/n}-1
\right]\times100
\]

Where \(n\) represents the number of months between the selected dates divided by 12.

For identical dates, the calculator reports an annualized change of 0% to avoid division by zero.

### Example Calculation

The following example compares **$100 in March 2000** with its equivalent value in **September 2026**.

```text
Enhanced Inflation Calculator
Monthly CPI: January 1914 - September 2026

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

### Interpretation

Based on the CPI data, a basket of goods and services costing **$100 in March 2000** would cost approximately **$179.32 in September 2026** if its price moved in line with the national CPI.

This represents:

- **79.32%** cumulative price growth.
- Approximately **2.23%** annualized inflation.
- A substantial reduction in the purchasing power of a fixed nominal dollar amount over the comparison period.

### Input Validation

The program includes validation to improve usability and prevent invalid calculations.

It checks that:

1. The monetary amount is positive and numeric.
2. Dates follow the `YYYY-MM` format.
3. Entered months are valid calendar months.
4. Both dates fall within the available dataset.
5. Invalid inputs are corrected before calculations proceed.

For example:

```text
Enter the price: $abc
Please enter a number, e.g. 100 or 1,250.50

Enter the price: $100

Enter the first date (YYYY-MM): March 2020
Please use the format YYYY-MM, e.g. 2020-03

Enter the first date (YYYY-MM): 2020-03
```

---

## Data Source and Methodology

**Primary Source:** [Bank of Canada — Inflation Calculator](https://www.bankofcanada.ca/rates/related/inflation-calculator/)

**Original Data Provider:** Statistics Canada

**Dataset:** Canadian Total Consumer Price Index, Monthly

**Base Year:** 2002 = 100

**Period Covered:** January 1914 – September 2026

### Data Processing

The Python programs use `pandas` to import, clean, and process the CPI dataset.

The CSV contains introductory metadata, which is skipped during import.

```python
import pandas as pd

data_frame = pd.read_csv("cpi.csv", skiprows=8)
```

Annual inflation is calculated using a 12-month percentage change:

```python
data_frame["Annual Pct Change"] = (
    data_frame["CPI"].pct_change(periods=12) * 100
)
```

This compares each month's CPI value with the corresponding month one year earlier.

---

## Conclusion

This project demonstrates how Python can be applied to financial data analysis through historical inflation measurement, visualization, and interactive calculations.

The CPI visualization illustrates long-term price changes and periods of inflation volatility in Canada.

The Enhanced Inflation Calculator extends the analysis by allowing users to quantify changes in purchasing power between specific months.

Together, these tools demonstrate practical applications of Python, pandas, and Matplotlib for working with economic and financial data.

---

**Course:** FINE 3300 — Python for Finance Professionals  
**Assignment:** Assignment 2, Part B  
**Author:** Krish Malhotra