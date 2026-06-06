# Chi-Square Test for Independence

![Python](https://img.shields.io/badge/Python-3.x-blue)
![SciPy](https://img.shields.io/badge/SciPy-Statistics-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Statistical analysis of customer product preferences using the **Chi-Square Test for Independence** with Python and SciPy.

---

## Project Description

This project demonstrates the practical application of the **Chi-Square Test for Independence**, a statistical method used to determine whether two categorical variables are associated. Using a retail marketing dataset, the analysis investigates whether customer gender influences preference for Product A or Product B.

The project includes both manual and automated statistical calculations. Manual computation illustrates the mathematical foundation of the Chi-Square Test, while Python's `scipy.stats.chi2_contingency()` function is used to validate the results.

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
|----------|----------|----------|
| Female | 2 | 4 |
| Male | 4 | 2 |

### Expected Frequencies

| Gender | Product A | Product B |
|----------|----------|----------|
| Female | 3 | 3 |
| Male | 3 | 3 |

---

## Installation

```bash
git clone https://github.com/rrmao-tech/chi-square-test-independence.git
cd chi-square-test-independence
pip install scipy pandas numpy
```

---

## Running the Analysis

### Manual Calculation

```bash
python test1.py
```

### Automated Calculation

```bash
python test2.py
```

---

## Example Output

```text
Chi-Square Statistic: 1.3333
Degrees of Freedom: 1
P-value: 0.2482

Decision:
Fail to reject the null hypothesis.

Conclusion:
No statistically significant relationship exists between
gender and product preference.
```

---

## Results

| Method | Chi-Square Statistic | p-value |
|----------|----------|----------|
| Manual Calculation | 1.33 | 0.2482 |
| SciPy Automated Test | 1.33 | 0.2482 |
| Yates' Correction | 0.33 | N/A |

---

## Business Implications

- Gender-based marketing segmentation may not be effective.
- Other variables such as age and purchasing behavior should be investigated.
- Statistical evidence should guide marketing decisions.

---

## Project Structure

```text
.
├── README.md
├── test1.py
├── test2.py
├── product.csv
├── ChiSquare_APA_Report.pdf
├── LICENSE
└── .gitignore
```

---

## Skills Demonstrated

- Statistical Analysis
- Hypothesis Testing
- Chi-Square Test of Independence
- Python Programming
- SciPy
- Data Interpretation
- Business Analytics
- APA Academic Reporting

---

## Author

**R.R.MAO**

GitHub: https://github.com/rrmao-tech
