# Statistical Engine & Monte Carlo Simulation

## Project Overview
This project implements a pure-Python statistical engine (`StatEngine`) that calculates **mean, median, variance, standard deviation, and detects outliers** from raw numerical data. It also includes a **Monte Carlo simulation** to model a startup server's daily crash probability and demonstrate the **Law of Large Numbers**.

## Mathematical Logic
- **Variance**: Measures how spread out the data is.  
  - Population variance: σ² = Σ(xᵢ - μ)² / N  
  - Sample variance: s² = Σ(xᵢ - x̄)² / (N - 1) (Bessel's correction)  

- **Median Calculation**:  
  - If the number of data points is **odd**, the median is the middle value of the sorted dataset.  
  - If **even**, the median is the average of the two middle values.  

## Setup and Run Instructions
Run the following commands in your terminal:

```bash
git clone https://github.com/nigussiemebatsion-sys/statistical_engine.git
cd statistical_engine
python main.py
python -m unittest discover tests
```
## Acceptance Criteria Checklist
- [x] Handles empty data lists without errors
- [x] Cleans non-numerical elements from input data
- [x] Accurately calculates mean, median, variance, standard deviation
- [x] Differentiates between population vs sample variance
- [x] Correctly identifies outliers
- [x] Monte Carlo simulation approximates server crash probability
- [x] Demonstrates Law of Large Numbers