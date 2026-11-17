
from sklearn.neighbors import KNeighborsClassifier 
income = [[20], [25], [35], [45], [55], [65]] 
classes = ["Low", "Low", "Medium", "Medium", "High", "High"] 
model = KNeighborsClassifier(n_neighbors=3) 
model.fit(income, classes) 
new_income = [[40]] 
prediction = model.predict(new_income) 
print("Income:", new_income[0][0]) 
print("Predicted Class:", prediction[0]) 