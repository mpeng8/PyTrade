'''
to connect to front end
'''
from datetime import date, timedelta
import SupervisedLearner

def predictStock(symb):
    predlen=7
    method='SVM'
    kwarg=None
    model = SupervisedLearner.SupervisedLearner(symb, predlen, method, kwarg)
    model.train()
    yesterday = date.today()-timedelta(1)
    time = yesterday.strftime('%F')
    result = model.querysingleday(yesterday)
    print result
    print yesterday
    return result

def predictStocksTimes(symb, startDate, endDate):
    #symb = 'AAPL'
    predlen=7
    method='SVM'
    kwarg=None
    model = SupervisedLearner.SupervisedLearner(symb, predlen, method, kwarg)
    model.train()
    result2 = model.querydates(startDate, endDate)
    return result2
