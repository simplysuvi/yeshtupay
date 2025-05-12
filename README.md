# Paycheck Estimator

A simple Streamlit app to estimate your gross and net pay based on your visa status (F1 or H1B) and annual salary.

## Features

- Choose between F1 (OPT/STEM) and H1B visa status
- Enter your annual salary
- View:
  - Semi-monthly (biweekly) gross and net pay
  - Monthly gross and net pay
  - Annual gross and net pay
- See detailed tax deductions per paycheck

## Tax Assumptions

This app uses higher-end estimates for deduction percentages:

| Deduction Type      | F1 (OPT/STEM) | H1B      |
|---------------------|---------------|----------|
| Federal Tax         | 11.81%        | 11.81%   |
| State Tax           | 4.79%         | 4.79%    |
| SDI + PFL           | 1.05%         | 1.05%    |
| Social Security     | ❌            | 6.20%    |
| Medicare            | ❌            | 1.45%    |

> F1 status does not include Social Security and Medicare deductions.


## Notes

* Assumes 24 pay periods (2 per month).
* Meant for estimation only; actual deductions may vary.
