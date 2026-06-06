# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

# Step 2: Load the dataset
df = pd.read_csv("product.csv")  # Ensure the CSV file is in the correct directory

# Step 3: Create a contingency table
contingency_table = pd.crosstab(df["Gender"], df["Preferred Product"])

# Step 4: Perform the Chi-Square Test automatically (without Yates' correction)
chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table, correction=False)

# Step 5: Display observed and expected frequencies
print("Observed Frequency Table:")
print(contingency_table)

print("\nExpected Frequencies (Calculated Automatically):")
expected_df = pd.DataFrame(expected, columns=contingency_table.columns, index=contingency_table.index)
print(expected_df)

# Step 6: Display test statistics
print("\nChi-square Statistic:", round(chi2_stat, 2))
print("P-value:", round(p_value, 4))
print("Degrees of Freedom:", dof)

# Step 7: Interpretation
alpha = 0.05
if p_value < alpha:
    print("\nWe reject the null hypothesis. Gender influences product preference.")
else:
    print("\nWe fail to reject the null hypothesis. Gender does not significantly influence product preference.")
