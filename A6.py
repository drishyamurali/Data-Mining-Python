import numpy as np
data = [12, 14, 15, 16, 17, 18, 19, 22, 95]
def detect_outliers_iqr(dataset):
    q1=np.percentile(dataset,25)
    q3=np.percentile(dataset,75)
    iqr=q3-q1
    lower_bound=q1-(1.5*iqr)
    upper_bound=q3-(1.5*iqr)
    outliers=[
        val for val in dataset if val<lower_bound or val>upper_bound
    ]
    return q1,q3,iqr,lower_bound,upper_bound,outliers
q1,q3,iqr,lower_bound,upper_bound,outliers=detect_outliers_iqr(data)
print(f"dataset:{data}")
print(f"q1(25th percentile):{q1}")
print(f"q3(75th percentile):{q3}")
print(f"iqr:{iqr}")
print(f"lower bound:{lower_bound}")
print(f"upper bound:{upper_bound}")
print(f"identified outliers:{outliers}")
