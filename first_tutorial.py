# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:26:33 2019

Test for scikit-learn system
@author: siirias
"""


from random import randint
from sklearn.linear_model import LinearRegression

TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 5

TRAIN_INPUT = list()
TRAIN_OUTPUT = list()
for i in range(TRAIN_SET_COUNT):
    a = randint(0, TRAIN_SET_LIMIT)
    b = randint(0, TRAIN_SET_LIMIT)
    c = randint(0, TRAIN_SET_LIMIT)
    op = a + (2*b) + (3*c)
    TRAIN_INPUT.append([a, b, c])
    TRAIN_OUTPUT.append(op)


predictor = LinearRegression(n_jobs=-1)
#LogisticRegression
predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)

X_TEST = [[10, 20, 30]]
outcome = predictor.predict(X=X_TEST)
coefficients = predictor.coef_

print('Outcome : {}\nCoefficients : {}'.format(outcome, coefficients))

