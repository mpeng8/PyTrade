'''
to connect to front end
'''

import SupervisedLearner

'''
configuration
'''
symb = 'AAPL'
predlen=7
method='RF'
kwarg=None

'''
script
'''
temp1 = SupervisedLearner.SupervisedLearner(symb, predlen, method, kwarg)
temp1.train()
a = temp1.querysingleday('2017-3-31')
b = temp1.querydates('2001-2-1', '2001-6-4')
print a
print b