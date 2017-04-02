from sklearn.neighbors import KNeighborsClassifier


'''
K nearest neighbout Learner
'''

class KNN:
    def __init__(self):
        self.learner = KNeighborsClassifier()

    def train(self,X,y):
        self.learner.fit(X,y)

    def query(self,X):
        rt = self.learner.predict(X)
        return rt

    def score(self,X,y):
        rt = self.learner.score(X,y)
        return rt