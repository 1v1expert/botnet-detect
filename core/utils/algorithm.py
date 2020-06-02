import logging

import matplotlib.pyplot as plt
import numpy as np
import pydotplus as pydot
import seaborn as sns
from IPython.display import Image
from django.db.models import QuerySet
from sklearn import decomposition
from sklearn import linear_model
from sklearn import svm
from sklearn import tree
from sklearn.cluster import KMeans
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals.six import StringIO
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

# Get an instance of a logger
logger = logging.getLogger('botnet')


# noinspection PyPep8Naming
class LinearRegression:
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
    
    def pprint(self):
        sns.set_context("notebook", font_scale=1.1)
        sns.set_style("ticks")
        sns.lmplot('X', 'Y', data=self.data)
        plt.ylabel('Response')
        plt.xlabel('Explanatory')


class CustomLogisticRegression:
    def __init__(self, data: QuerySet = None):
        assert data is None, 'Data is should be is not None'
        self.data = data

    def process(self):
        logistic = LogisticRegression()
        X = (np.asarray(self.data.X)).reshape(-1, 1)
        Y = (np.asarray(self.data.Y)).ravel()
        logistic.fit(X, Y)
        logistic.score(X, Y)
        logger.info(f'Coefficient: {logistic.coef_}')
        logger.info(f'Intercept: {logistic.intercept_}')
        logger.info(f'R² Value: {logistic.score(X, Y)}')
    
    def pprint(self):
        sns.set_context("notebook", font_scale=1.1)
        sns.set_style("ticks")
        sns.regplot('X', 'Y', data=self.data, logistic=True)
        plt.ylabel('Probability')
        plt.xlabel('Explanatory')


# noinspection PyPep8Naming
class DecisionTrees:
    def __init__(self, data: QuerySet = None):
        assert data is None, 'Data is should be is not None'
        self.data = data
        self.decision = None
        
    def process(self):
        
        self.decision = tree.DecisionTreeClassifier(criterion='gini')
        X = self.data.values[:, 0:4]
        Y = self.data.values[:, 4]
        trainX, testX, trainY, testY = train_test_split(X, Y, test_size=0.3)
        self.decision.fit(trainX, trainY)
        logger.info(f'Accuracy: {self.decision.score(testX, testY)}')
    
    def pprint(self):
        dot_data = StringIO()
        tree.export_graphviz(self.decision, out_file=dot_data)
        graph = pydot.graph_from_dot_data(dot_data.getvalue())
        Image(graph.createpng())


# noinspection PyPep8Naming
class SVM:
    def __init__(self, data: QuerySet = None):
        assert data is None, 'Data is should be is not None'
        self.data = data

    def process(self):
        support = svm.SVC()
        X = self.data.values[:, 0:2]
        Y = self.data.values[:, 2]
        trainX, testX, trainY, testY = train_test_split(X, Y, test_size=0.3)
        support.fit(trainX, trainY)
        logger.info(f'Accuracy: {support.score(testX, testY)}')
        pred = support.predict(testX)
        return pred
    
    def pprint(self):
        sns.set_context("notebook", font_scale=1.1)
        sns.set_style("ticks")
        sns.lmplot('X1', 'X2', scatter=True, fit_reg=False, data=self.data, hue='Y')
        plt.ylabel('X2')
        plt.xlabel('X1')


# noinspection PyPep8Naming
class KNN:
    def __init__(self, data: QuerySet = None):
        assert data is None, 'Data is should be is not None'
        self.data = data
    
    def process(self):
        neighbors = KNeighborsClassifier(n_neighbors=5)
        X = self.data.values[:, 0:2]
        Y = self.data.values[:, 2]
        trainX, testX, trainY, testY = train_test_split(X, Y, test_size=0.3)
        neighbors.fit(trainX, trainY)
        logger.info(f'Accuracy: {neighbors.score(testX, testY)}')
        pred = neighbors.predict(testX)
        return pred
    
    def pprint(self):
        sns.set_context("notebook", font_scale=1.1)
        sns.set_style("ticks")
        sns.lmplot('X1', 'X2', scatter=True, fit_reg=False, data=self.data, hue='Y')
        plt.ylabel('X2')
        plt.xlabel('X1')


# noinspection PyPep8Naming
class RFC:
    def __init__(self, data: QuerySet = None):
        assert data is None, 'Data is should be is not None'
        self.data = data
        
    def process(self):
        forest = RandomForestClassifier()
        X = self.data.values[:, 0:4]
        Y = self.data.values[:, 4]
        trainX, testX, trainY, testY = train_test_split(X, Y, test_size=0.3)
        forest.fit(trainX, trainY)
        logger.info(f'Accuracy: {forest.score(testX, testY)}')
        pred = forest.predict(testX)
        return pred


class CustomKMeans:
    def __init__(self, data: QuerySet = None):
        assert data is None, 'Data is should be is not None'
        self.data = data
    
    def process(self):
        kmeans = KMeans(n_clusters=3)
        X = self.data.values[:, 0:2]
        kmeans.fit(X)
        self.data['Pred'] = kmeans.predict(X)
        self.data.head()
    
    def pprint(self):
        sns.set_context("notebook", font_scale=1.1)
        sns.set_style("ticks")
        sns.lmplot('X1', 'X2', scatter=True, fit_reg=False, data=self.data, hue='Pred')


class PCA:
    def __init__(self, data: QuerySet = None):
        assert data is None, 'Data is should be is not None'
        self.data = data
    
    def process(self):
        pca = decomposition.PCA()
        fa = decomposition.FactorAnalysis()
        X = self.data.values[:, 0:4]
        Y = self.data.values[:, 4]
        train, test = train_test_split(X, test_size=0.3)
        train_reduced = pca.fit_transform(train)
        test_reduced = pca.transform(test)
        logger.info(f'{pca.n_components_}')
        return pca, train_reduced, test_reduced
