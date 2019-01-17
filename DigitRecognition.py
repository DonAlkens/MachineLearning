import numpy as np

from sklearn.datasets import load_digits
from sklearn.svm import SVC
from scipy import misc

digits = load_digits()

features = np.array(digits.data)
label = np.array(digits.target)

clf = SVC(gamma = 0.001)
clf.fit(features, label)

# print(clf.predict(features[-1].reshape(1,-1)))

img = misc.imread("images/2.jpg")
img = misc.imresize(img, (8,8))
img = img.astype(digits.images.dtype)
img = misc.bytescale(img, high=16, low=0)

x_test = []

for eachRow in img:
	for eachPixels in eachRow:
		x_test.append(sum(eachPixels)/3.0)


print(clf.predict([x_test]))