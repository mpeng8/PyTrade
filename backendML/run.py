'''
to connect to front end
'''

import SupervisedLearner

symb = 'AAPL'
predlen=7
method='RF'
kwarg=None

model = SupervisedLearner.SupervisedLearner(symb, predlen, method, kwarg)
model.train()
result = model.querysingleday('2017-3-31')
result2 = model.querydates('2001-2-1', '2001-6-4')
print result
print result2