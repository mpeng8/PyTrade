import unit
import RF
import SVM
import KNN
import NN
import pandas as pd 
import numpy as np 
import sklearn
from sklearn.model_selection import cross_val_score
import util


'''
Supervised learner wrapper

SVM, KNN, RF, NN
'''

class SupervisedLearner(object):

    def __init__(self, symb, predlen, cat='RL',kwargs=None):

        self.symb = symb
        self.predlen = predlen
        self.kwargs = kwargs
        self.cat = cat

        if cat=='RF':
            if kwargs != None:
                self.learner = RF.RandomForest(**kwargs)
            else:
                self.learner = RF.RandomForest()

        elif cat == 'KNN':
            if kwargs != None:
                self.learner = KNN.KNN(**kwargs)
            else:
                self.learner = KNN.KNN()

        elif cat == 'SVM':
            if kwargs != None:
                self.learner = SVM.SVM(**kwargs)
            else:
                self.learner = SVM.SVM()

        elif cat=='NN':
            if kwargs != None:
                self.learner = NN.NN(**kwargs)
            else:
                self.learner = NN.NN()



    def train(self,trainsd = '2016-6-4', trained='2017-1-10'):
        trainunit = unit.Unit(self.symb,trainsd,trained, self.predlen)
        trainxy = trainunit.preprocessRF()
        trainx = trainxy[:,:-1]
        trainy = trainxy[:,-1]        
        self.learner.train(trainx,trainy)


    '''
    predict last day
    '''
    def querysingleday(self,date):
        sd = '2017-1-1'
        ed = date

        testunit = unit.Unit(self.symb, sd, ed, self.predlen)
        testx = testunit.preprocessRF(mode=2)
        predy = self.learner.query(testx)

        res = predy[-1]

        #need modification

        if res>0.3:
            return 'buy'
        elif res < -0.3:
            return 'sell'
        else:
            return 'watch'



    '''
    return result of backtesting

    '''
    def querydates(self,sd, ed):
        sd = util.minusdate(sd)
        testunit = unit.Unit(self.symb, sd, ed, self.predlen)
        testx = testunit.preprocessRF(mode=2)
        predy = self.learner.query(testx)
        res = testunit.convert2(predy)
        res.dropna()

        print res

        for i in range(len(res)):
            if res.ix[i,0] > 0.3:
                res.ix[i, 0] = 'buy'
            elif res.ix[i, 0] < -0.3:
                res.ix[i,0] = 'sell'
            else:
                res.ix[i,0] = 'watch'

        return res





    def test(sd, ed):
        testunit = Unit(self.symb, sd, ed, self.predlen)
        testx = unit.preprocessRF(mode=2)
        predy = self.learner.query(testx)
        temp = testunit.convert2(predy)
        realy = testunit.labelreturn()
        temp2 = pd.concat([temp, realy], axis=1)
        temp2.dropna()


    '''
    for demo only. Not convert the result to str label
    '''
    def crossvaltest(self,sd, ed):
        unit1 = unit.Unit(self.symb, sd, ed, self.predlen)
        testx = unit1.preprocessRF()
        xx = testx[:,:-1]
        yy = testx[:,-1]

        print xx.shape

        print yy.shape

        if self.cat=='RF':
            clf = sklearn.ensemble.RandomForestClassifier(n_estimators=25)
        elif self.cat == 'KNN':
            clf = sklearn.neighbors.KNeighborsClassifier()
        elif self.cat =='SVM':
            clf = sklearn.svm.SVC()
        elif self.cat=='NN':
            clf = sklearn.neural_network.MLPClassifier()
        
        accu = cross_val_score(clf, xx, yy, cv=3)
        #precision = cross_val_score(clf, xx, yy, cv=10, scoring='precision')
        #recall = cross_val_score(clf,xx,yy,cv=10,scoring='recall')

        print accu
        #print precision
        #print recall

        print 'mean:'
        print 'accu: '+str(np.mean(accu))
        #print 'precision: ' + str(np.mean(precision))
        #print 'recall: ' + str(np.mean(recall))






