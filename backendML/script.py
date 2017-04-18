

symb='AAPL'
x = [3,5,7,10,15]
y = [['2005-6-4', '2006-1-10'], ['2013-6-4','2014-1-10'], ['2016-6-4','2017-1-10']]
y2=[['2003-6-4', '2006-1-10'], ['2011-6-4','2014-1-10'], ['2014-6-4','2017-1-10']]





import SupervisedLearner


def hehe(symb, method, x, y):

    print symb
    print method
    for yy in y:
        for xx in x:
            print 'time sel: ' + yy[0] + ' ~ ' + yy[1]
            print 'predlen: '+ str(xx) 
            temp = SupervisedLearner.SupervisedLearner(symb, xx, method)
            temp.crossvaltest(yy[0],yy[1])

def gg():
    symb = 'AAPL'
    method = 'SVM'
    hehe(symb, method, x, y2)
    #hehe(symb,method,x,y2)

gg()

# temp1 = SupervisedLearner.SupervisedLearner(symb, , 'NN')
# temp1.crossvaltest('2005-6-4', '2006-1-10')

# temp2 = SupervisedLearner.SupervisedLearner(symb, , 'NN')
# temp2.crossvaltest('2005-6-4', '2006-1-10')

# temp3 = SupervisedLearner.SupervisedLearner(symb, , 'NN')
# temp3.crossvaltest('2005-6-4', '2006-1-10')

# temp4 = SupervisedLearner.SupervisedLearner(symb, , 'NN')
# temp4.crossvaltest('2005-6-4', '2006-1-10')

# temp5 = SupervisedLearner.SupervisedLearner(symb, , 'NN')
# temp5.crossvaltest('2005-6-4', '2006-1-10')

# temp1 = SupervisedLearner.SupervisedLearner(symb, )
# temp1.crossvaltest('2013-6-4', '2014-1-10')

# temp2 = SupervisedLearner.SupervisedLearner(symb, )
# temp2.crossvaltest('2013-6-4', '2014-1-10')

# temp3 = SupervisedLearner.SupervisedLearner(symb, )
# temp3.crossvaltest('2013-6-4', '2014-1-10')

# temp4 = SupervisedLearner.SupervisedLearner(symb, )
# temp3.crossvaltest('2013-6-4', '2014-1-10')

# temp4 = SupervisedLearner.SupervisedLearner(symb, , 'NN')
# temp5.crossvaltest('2013-6-4', '2014-1-10')

# temp1 = SupervisedLearner.SupervisedLearner(symb, )
# temp1.crossvaltest('2016-6-4', '2017-1-10')

# temp2 = SupervisedLearner.SupervisedLearner(symb, )
# temp2.crossvaltest('2016-6-4', '2017-1-10')

# temp3 = SupervisedLearner.SupervisedLearner(symb, )
# temp3.crossvaltest('2016-6-4', '2017-1-10')

# temp3 = SupervisedLearner.SupervisedLearner(symb, )
# temp3.crossvaltest('2016-6-4', '2017-1-10')