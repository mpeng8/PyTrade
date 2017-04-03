from sklearn.ensemble import RandomForestClassifier

'''
Random Forest Learner
'''

class RandomForest(object):

    def __init__(self, kwargs=None):

        if kwargs== None:
            self.learner = RandomForestClassifier()
        else:
            self.learner = RandomForestClassifier(**kwargs)


    def train(self,X,y):
        self.learner.fit(X,y)

    def query(self,X):
        rt = self.learner.predict(X)
        return rt

    def score(self,X,y):
        rt = self.learner.score(X,y)
        return rt