'''
to connect to front end
'''

import SupervisedLearner

def predictStock(symb):
    #symb = 'AAPL'
    predlen=7
    method='RF'
    kwarg=None
    model = SupervisedLearner.SupervisedLearner(symb, predlen, method, kwarg)
    model.train()

    result = model.querysingleday('2017-3-31')
    print result
    #result2 = model.querydates('2001-2-1', '2001-6-4')
    return result
    #print result2
