# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:43:33 2019

@author: siirias
"""
import datetime
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn import svm
import pickle
import joblib

digits = datasets.load_digits()  #esimerkkidata
plt.imshow(np.reshape(digits.data[0],(8,8))) #show one example

clf = svm.SVC(gamma=0.001, C=100.) #support vector classification
clf.fit(digits.data[:-1], digits.target[:-1])
#running fit again overwrites earlier lessons.
#

clf.predict(digits.data[-1:])
print(clf.score(digits.data[:-1], digits.target[:-1]))

#saving this predictor
#s = pickle.dumps(clf)
#clf=pickle.load(s)
#better or big data:
joblib.dump(clf,'testdave.clf')
#loading:
