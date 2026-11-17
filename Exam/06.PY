#Guassian Navie Bayes

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
hours=[[2],[3],[4],[5],[6],[7]]
result=["Fail","Fail","Pass","Pass","Pass","Pass"]
model=GaussianNB()
model.fit(hours,result)
prediction=model.predict([[5]])
print("Prediction=",prediction)
train_prediction=model.predict(hours)
accuracy=accuracy_score(result,train_prediction)
print("Accuracy=",accuracy)