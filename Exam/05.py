#KMeans

from sklearn.cluster import KMeans
X=[
    [22,20],
    [25,25],
    [28,30],
    [40,70],
    [42,75],
    [45,80]
]
model=KMeans(n_clusters=2, random_state=0)
model.fit(X)
for i in range(len(X)):
    print(X[i],"Cluster =",model.labels_[i])