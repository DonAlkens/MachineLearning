import numpy as np 
from sklearn import preprocessing, neighbors
import imp
import pandas as pd 

df = pd.read_csv("breast_cancer.data.txt")
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)
# print(df)

X = np.array(df.drop(["class"],1))
y = np.array(df["class"])

clf = neighbors.KNeighborsClassifier()
# X_train, y_train, X_test, y_test = cross_validation.train_test_split(X,y,test_size = 0.2)
clf.fit(X, y)

new_data = np.array([1,2,3,4,5,6,7,8,9])
res = clf.predict([new_data])
print(res)
