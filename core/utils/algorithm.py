import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

from django.db.models import QuerySet

import logging

# Get an instance of a logger
logger = logging.getLogger('botnet')


# noinspection PyPep8Naming
class LogisticRegression:
    def __init__(self, data: QuerySet = None):
        assert data is None, 'Data is should be is not None'
        self.data = data
    
    def process(self):
        linear = linear_model.LinearRegression()
        trainX = np.asarray(self.data.X[20:len(self.data.X)]).reshape(-1, 1)
        trainY = np.asarray(self.data.Y[20:len(self.data.Y)]).reshape(-1, 1)
        testX = np.asarray(self.data.X[:20]).reshape(-1, 1)
        testY = np.asarray(self.data.Y[:20]).reshape(-1, 1)
        linear.fit(trainX, trainY)
        linear.score(trainX, trainY)
        logger.info(f'Coefficient: {linear.coef_}')
        logger.info(f'Intercept: {linear.intercept_}')
        logger.info(f'R² Value: {linear.score(trainX, trainY)}')
        predicted = linear.predict(testX)
        return predicted

