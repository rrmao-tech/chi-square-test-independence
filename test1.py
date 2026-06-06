# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
from scipy.stats import chi2

# Step 2: Load the dataset
df = pd.read_csv("product.csv")

# Step 3: Create a contingency table
contingency_table = pd.crosstab(df["Gender"], df["Preferred Product"])

# Step 4: Calculate row and column totals
row_totals = contingency_table.sum(axis=1)
col_totals = contingency_table.sum(axis=0)
grand_total = contingency_table.values.sum()

# Step 5: Compute expected frequencies manually
expected_frequencies = np.outer(row_totals, col_totals) / grand_total

# Step 6: Compute the Chi-Square statistic manually
chi_square_statistic = ((contingency_table - expected_frequencies) ** 2 / expected_frequencies).sum().sum()

# Step 7: Compute p-value manually
dof = (contingency_table.shape[0] - 1) * (contingency_table.shape[1] - 1)
p_value = 1 - chi2.cdf(chi_square_statistic, df=dof)

# Step 8: Display observed and expected frequencies
print("Observed Frequency Table:")
print(contingency_table)

print("\nExpected Frequencies (Calculated Manually):")
expected_df = pd.DataFrame(expected_frequencies, columns=contingency_table.columns, index=contingency_table.index)
print(expected_df)

# Step 9: Display test statistic
print("\nManual Chi-square Statistic:", round(chi_square_statistic, 2))
print("P-value (Calculated Manually):", round(p_value, 4))
print("Degrees of Freedom:", dof)

# Step 10: Interpretation
alpha = 0.05
if p_value < alpha:
    print("\nWe reject the null hypothesis. Gender influences product preference.")
else:
    print("\nWe fail to reject the null hypothesis. Gender does not significantly influence product preference.")
