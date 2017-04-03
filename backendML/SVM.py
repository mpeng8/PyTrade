from sklearn.svm import SVC

'''
Support Vector Machine Learner

'''

class SVM:

    def __init__(self, kwargs=None):
        if kwargs==None:
            self.learner = SVC()
        else:
            self.learner = SVC(**kwargs)

    def train(self,X,y):
        self.learner.fit(X,y)

    def query(self,X):
        rt = self.learner.predict(X)
        return rt

    def score(self,X,y):
        rt = self.learner.score(X,y)
        return rt

