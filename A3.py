import numpy as np

# Input data
study_hours = [2, 3, 4, 5, 6, 7]
marks = [40, 50, 60, 70, 80, 90]

# Calculate Pearson Correlation Coefficient
correlation = np.corrcoef(study_hours, marks)

# Display correlation matrix
print("Correlation Matrix:")
print(correlation)

# Display Pearson correlation coefficient
print("\nPearson Correlation Coefficient:")
print(correlation[0][1])

