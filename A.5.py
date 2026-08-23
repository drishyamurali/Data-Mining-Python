from sklearn.neighbors import KNeighborsClassifier
import numpy as np
# Training data
income = [[20], [25], [35], [45], [55], [65]]
# Corresponding customer classes
customer_class = ["Low", "Low", "Medium", "Medium", "High", "High"]
# Step 1: Create KNN classifier
# K = 3
knn_model = KNeighborsClassifier(n_neighbors=3)
# Step 2: Train the model
knn_model.fit(income, customer_class)
print("KNN Model trained successfully!")
print("Training Data (Income):", income)
print("Training Labels (Class):", customer_class)
print("-" * 30)
# Step 3: Define new customer
new_customer_income = [[40]]
# Step 4: Predict the class
prediction = knn_model.predict(new_customer_income)
print(f"New Customer Income: {new_customer_income[0][0]}")
print(f"Predicted Class: {prediction[0]}")
