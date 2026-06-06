# Chi-Square Test

![Python](https://img.shields.io/badge/Python-3.12-blue)
![SciPy](https://img.shields.io/badge/SciPy-Statistics-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Statistical analysis of customer product preferences using the Chi-Square Test for Independence.

# Chi-Square Test for Independence

## Overview

This project investigates whether **product preference** is independent of **gender** using the **Chi-Square Test for Independence**. The analysis includes both a manual calculation and an automated statistical test using Python.

## Scenario

A retail company surveyed **12 customers** and recorded:

- Gender (Male or Female)
- Preferred Product (Product A or Product B)

The objective is to determine whether gender has a statistically significant influence on product preference.

---

## Research Question

**Does gender influence customer product preference?**

### Null Hypothesis (H₀)
Gender and product preference are independent.

### Alternative Hypothesis (H₁)
Gender and product preference are associated.

---

## Dataset

### Observed Frequencies

| Gender | Product A | Product B |
|---------|-----------|-----------|
| Female | 2 | 4 |
| Male | 4 | 2 |

### Expected Frequencies (Assuming Independence)

| Gender | Product A | Product B |
|---------|-----------|-----------|
| Female | 3 | 3 |
| Male | 3 | 3 |

---

## Methodology

### Manual Chi-Square Calculation

The Chi-Square statistic is calculated using:

χ² = Σ((Observed − Expected)² / Expected)

Calculations:

- (2 − 3)² / 3 = 0.3333
- (4 − 3)² / 3 = 0.3333
- (4 − 3)² / 3 = 0.3333
- (2 − 3)² / 3 = 0.3333

Total:

**χ² = 1.3333**

### Degrees of Freedom

df = (rows − 1) × (columns − 1)

df = (2 − 1) × (2 − 1) = 1

---

## Python Implementation

### Manual Calculation

```bash
python test1.py
```

### Automated Calculation Using SciPy

```bash
python test2.py
```

The automated test uses:

```python
from scipy.stats import chi2_contingency
```

---

## Results

| Method | Chi-Square Statistic | p-value |
|----------|--------------------|---------|
| Manual Calculation | 1.33 | 0.2482 |
| SciPy Automated Test | 1.33 | 0.2482 |
| Yates' Correction | 0.33 | N/A |

---

## Statistical Interpretation

- Significance level (α): 0.05
- Calculated p-value: 0.2482

Since:

0.2482 > 0.05

we **fail to reject the null hypothesis**.

### Conclusion

There is **no statistically significant association** between gender and product preference in this dataset.

The observed differences are likely due to random variation rather than a meaningful relationship.

---

## Business Implications

Because gender does not appear to significantly influence product selection:

- Gender-based marketing segmentation may not be effective.
- The company should investigate other variables such as:
  - Age
  - Purchasing behavior
  - Customer preferences
  - Shopping frequency

These factors may provide stronger insights for targeted marketing strategies.

---

## Project Structure

```text
.
├── test1.py      # Manual Chi-Square calculation
├── test2.py      # Automated Chi-Square test using SciPy
└── README.md     # Project documentation
```

---

## Key Learning Outcomes

- Understanding categorical data analysis
- Applying the Chi-Square Test for Independence
- Comparing manual and automated statistical methods
- Interpreting p-values and hypothesis tests
- Drawing business conclusions from statistical evidence

---

## Submission Statement

This assessment was completed by applying both manual and automated Chi-Square Tests of Independence to evaluate the relationship between gender and product preference.

Both methods produced consistent results:

- χ² ≈ 1.33
- p ≈ 0.2482

Because the p-value exceeds the 0.05 significance threshold, the null hypothesis was not rejected. Therefore, there is insufficient evidence to conclude that gender influences product preference within this sample.
