import pandas as pd

# Create the dataset
data = {
    "Name": ["Anil", "Bharath ", "Charan", "Deepa", "Farah"],
    "Age": [24, 26, 25, 28, 27],
    "Salary": [35000, 42000, None, 50000, 48000]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Step 1: Data Selection
selected_data = df[["Name", "Age", "Salary"]]

# Step 2: Data Preprocessing
# Replace missing salary with mean salary
selected_data["Salary"] = selected_data["Salary"].fillna(
    selected_data["Salary"].mean()
)

# Step 3: Data Transformation
# Convert Salary into integer
selected_data["Salary"] = selected_data["Salary"].astype(int)

print("\nFinal Transformed Dataset:")
print(selected_data)
