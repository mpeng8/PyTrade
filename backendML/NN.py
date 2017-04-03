from sklearn.neural_network import MLPClassifier

class NN:
    def __init__(self):
        self.learner = MLPClassifier()

    def train(self,X,y):
        self.learner.fit(X,y)

    def query(self,X):
        rt = self.learner.predict(X)
        return rt

    def score(self,X,y):
        rt = self.learner.score(X,y)
        return rt

