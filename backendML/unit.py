import pandas as pd
import numpy as np
import util
from talib.abstract import *

'''
sd, ed, symb from frontend

format

symb 

pred date = x

sd = '2001-1-1'
ed = '2010-1-1'

#
Random forest indicator sel = [K, RSI,WILLR,MACD,OBV,PROC]


'''

class Unit:

    def __init__(self, symb, sd, ed, predlen=7):
        self.sd = sd
        self.predlen = predlen
        self.ed = ed
        df = util.get_quandl(sd,ed,symb)
        df = df.rename(index=str, columns={'Close':'close', 'Open':'open', 'High':'high', 'Low':'low', 'Volume':'volume'})
        self.df = df
        self.index = df.index

    '''
    preprocessing. Exponentially smoothing data
    '''
    def expsmoothing(self,df, alpha = 1):
        df = df*alpha + df.shift(1)*(1-alpha)
        return df

    '''
    For Random Forest only
    preprocessing data 
    return numpy matrix
    mode=1=train; else=test
    '''
    def preprocessRF(self,mode=1):
        dfx = self.expsmoothing(self.df)
        X = self.addXRF(dfx)

        print X.shape
        if mode==1:
            Y = self.addYRF(self.df)

            print Y.shape
            rt = pd.concat([X,Y], axis=1)
            rt = rt.dropna()

            print rt.shape
            return rt.as_matrix()
        else:
            X = X.dropna()
            return X.as_matrix()



    '''
    For Random Forest only
    add indicators = [K, RSI,WILLR,MACD,OBV,PROC]
    return pd dataframe
    '''
    def addXRF(self,df):
        k = STOCH(df)['slowk']
        rsi = RSI(df)
        willr = WILLR(df)
        #obv = OBV(df)
        macd = MACD(df)['macd']
        proc = ROCP(df, self.predlen)

        rt = pd.concat([k, rsi, willr, macd, proc], axis=1)

        print rt.shape
        return rt

    '''
    For Random Forest only
    threshold label
    return panda dataframe
    '''
    def addYRF(self,df):
        temp = df['close']
        temp = temp-temp.shift(-self.predlen)


        return np.sign(temp)


    '''
    normalizing log return of date length of x=predlen

    return panda dataframe
    '''
    def logreturn(self,df):
        price = df['close']
        logr = (np.log(price/price.shift(self.predlen)))/self.predlen
        return logr

    '''
    threshold return

    return panda dataframe
    '''
    def labelreturn(self):
        price = self.df['close']
        dr = np.sign(price-price.shift(self.predlen))
        return dr

        
    '''
    convert df to np matrix
    '''
    def convert(self):
        df2 = self.df.as_matrix(columns=self.colsel)
        return df2


    '''
    convert np matrix to df
    '''
    def convert2(self,arr):
        df3 = pd.DataFrame(data=arr, index=self.index[34:])
        return df3