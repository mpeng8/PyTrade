'''
for demo only

run crossvalidation for various setting to generate report

'''


import SupervisedLearner

temp1 = SupervisedLearner.SupervisedLearner('AAPL', 7, 'KNN')
temp1.crossvaltest('2005-6-4', '2006-1-10')

temp2 = SupervisedLearner.SupervisedLearner('AAPL', 3, 'KNN')
temp2.crossvaltest('2005-6-4', '2006-1-10')

temp3 = SupervisedLearner.SupervisedLearner('AAPL', 10, 'KNN')
temp3.crossvaltest('2005-6-4', '2006-1-10')

temp3 = SupervisedLearner.SupervisedLearner('AAPL', 5, 'KNN')
temp3.crossvaltest('2005-6-4', '2006-1-10')

# temp1 = SupervisedLearner.SupervisedLearner('AAPL', 7)
# temp1.crossvaltest('2013-6-4', '2014-1-10')

# temp2 = SupervisedLearner.SupervisedLearner('AAPL', 3)
# temp2.crossvaltest('2013-6-4', '2014-1-10')

# temp3 = SupervisedLearner.SupervisedLearner('AAPL', 10)
# temp3.crossvaltest('2013-6-4', '2014-1-10')

# temp3 = SupervisedLearner.SupervisedLearner('AAPL', 5)
# temp3.crossvaltest('2013-6-4', '2014-1-10')

# temp1 = SupervisedLearner.SupervisedLearner('AAPL', 7)
# temp1.crossvaltest('2016-6-4', '2017-1-10')

# temp2 = SupervisedLearner.SupervisedLearner('AAPL', 3)
# temp2.crossvaltest('2016-6-4', '2017-1-10')

# temp3 = SupervisedLearner.SupervisedLearner('AAPL', 10)
# temp3.crossvaltest('2016-6-4', '2017-1-10')

# temp3 = SupervisedLearner.SupervisedLearner('AAPL', 5)
# temp3.crossvaltest('2016-6-4', '2017-1-10')