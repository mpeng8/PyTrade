from sklearn.ensemble import RandomForestClassifier

'''
Random Forest Learner
'''

class RandomForest:

    def __init__(self, treenum=10):

        self.learner = RandomForestClassifier(n_estimators=10)


    def train(self,X,y):
        self.learner.fit(X,y)

    def query(self,X):
        rt = self.learner.predict(X)
        return rt

    def score(self,X,y):
        rt = self.learner.score(X,y)
        return rt