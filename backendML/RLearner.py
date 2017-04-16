import datetime as dt
import QLearner as ql
import pandas as pd
import util as ut
import numpy as np
import unit

'''
Reinforcement Learner 
'''

class RLearner(object):

    # constructor
    def __init__(self, verbose = False):
        self.verbose = verbose
        ###### config ##########
        self.bucket = 10
        self.idct = 3 
        self.maxiter = 35
        self.miniter = 15
        self.threshold = None


  
    def addEvidence(self, symbol = 'AAPL', sd='2007-1-1', ed='2008-1-1', sv = 10000): 

        self.learner = ql.QLearner()

        prices = ut.get_quandl(sd ,ed, symbol)
        prices = prices['Close']

        if self.verbose: print prices

        dtlen = len(prices)
        self.dtlen = dtlen



        df = self.addIndicators(prices.copy(), syms)
        self.addthreshold(df.copy(), syms)
        self.QLearner = ql.QLearner(num_states=self.bucket**self.idct, num_actions=3, dyna=0,rar = 0.9,radr = 0.9999)
        self.train(df, syms, sv)
        #print self.QLearner.Q

        

    def train(self,df,symb,sv):

        #indicators = np.asarray(df[['BBV','k','vol']].copy().dropna())
        indicators = np.asarray(df[['BBV','ppo','vol']].copy().dropna())
        statesss = np.zeros(len(indicators))
        for i in range(len(indicators)):
            statesss[i] = self.querystate(indicators[i,0],indicators[i,1],indicators[i,2])

        #print(statesss)


        iterr = 0

        pos = 0 # pos 0 = nothing, pos 1 = long, pos 2 = short
        stock = 0
        cash = sv
        converge = False
        oldval = sv

        self.curstate = statesss[0]
        delta = self.dtlen-len(indicators)
        actionls = []
        actionlsprev = [0 for i in range(len(indicators))]
        prevtemp = 2333

        df['record'] = 0.0


        #port_val = np.full(df.shape[0], sv)

        while iterr<self.miniter or (not converge and iterr<self.maxiter):

            
            initstate = statesss[0]
            action = self.QLearner.querysetstate(initstate)
            actionls = []
            actionls.append(action)
            accur = 0

            for j in range(delta+1, self.dtlen):

                tradeprice = df.ix[j, symb].values[0]

                if action==1:
                    if pos == 0:                        
                        cash -= 500*tradeprice
                        df.ix[j, 'record'] = 500.0            
                    elif pos ==2:
                        cash -= 1000*tradeprice
                        df.ix[j, 'record'] = 1000.0
                    stock = 500
                    pos = 1
                elif action==2:
                    if pos == 0:
                        cash += 500*tradeprice   
                        df.ix[j, 'record'] = -500.0         
                    elif pos ==1:
                        cash += 1000*tradeprice
                        df.ix[j, 'record'] = -1000.0
                    stock = -500
                    pos = 2
                else:
                    if pos == 1:
                        cash += 500*tradeprice
                        df.ix[j, 'record'] = -500.0
                    elif pos ==2:
                        cash -= 500*tradeprice
                        df.ix[j, 'record'] = 500.0
                    stock = 0
                    pos = 0   

                val = cash + stock*tradeprice

                

                r = ((val/oldval)-1)*500

                accur+=r

                action = self.QLearner.query(statesss[j-delta], r)
                actionls.append(action)

                oldval = val

  

            # for i in range(len(indicators)):
            #     temp += abs(actionls[i] - actionlsprev[i])
            temp = sum(abs(actionls[i]-actionlsprev[i]) for i in range(len(indicators)))



            
            # if (accur<0 or val<sv*0.92):
            # #if (temp>100 and temp>0.99*prevtemp):
            #     self.QLearner.rar = 0.9
            #     actionlsprev = [0 for i in range(len(indicators))]
            #     self.QLearner.Q = np.random.uniform(low = -1.0, high = 1.0, size=(self.bucket**self.idct, 3))
            #     prevtemp = 2333
            # else:
            actionlsprev = actionls
            prevtemp = temp

            print(temp)
            print(accur)
            #print(self.QLearner.rar)

            if temp < 12 or (r> 10 and val>sv*2.5):
                converge = True

            iterr +=1
            print(iterr)

        print(val)
        print(df['record'])
        print(tradeprice)






    # this method should use the existing policy and test it against new data
    def testPolicy(self, symbol = 'AAPL', \
        sd='2009-1-1', \
        ed='2010-1-1', \
        sv = 10000):

        trades = ut.get_quandl(sd,ed,symbol)
        trades = df['Close']

        dtlen = len(trades)

        df = self.addIndicators(trades, [symbol])
        df['port_val'] = sv

        record[symbol] = 0.0
        record['adv'] = 'watch'

        cash = sv
        pos = 0
        stock = 0

        #indicators = np.asarray(df[['BBV','k','vol']].copy().dropna())
        #indicators = np.asarray(df[['BBV','mom','vol']].copy().dropna())
        indicators = np.asarray(df[['BBV','ppo','vol']].copy().dropna())
        
        #print(indicators)
        statesss = np.zeros(indicators.shape[0])

        print(len(statesss))
        for i in range(len(indicators)):
            statesss[i] = self.querystate(indicators[i,0],indicators[i,1],indicators[i,2])

        print(statesss)


        delta = dtlen-len(indicators)
        initprice = df.ix[0, symbol]


        for j in range(delta+1,dtlen):

            tradeprice = df.ix[j, symbol]

            action = self.QLearner.querysetstate(statesss[j-delta])

            if action==1:
                if pos == 0:                        
                    cash -= 500*tradeprice   
                    record.ix[j,symbol] = 500.0    
                    record.ix[j,'adv'] = 'buy' 
                elif pos ==2:
                    cash -= 1000*tradeprice
                    record.ix[j,symbol] = 1000.0
                    record.ix[j,'adv'] = 'buy' 
                stock = 500
                pos = 1
            elif action==2:
                if pos == 0:
                    cash += 500*tradeprice  
                    record.ix[j,symbol] = -500.0 
                    record.ix[j,'adv'] = 'sell'          
                elif pos ==1:
                    cash += 1000*tradeprice
                    record.ix[j,symbol] = -1000.0
                    record.ix[j,'adv'] = 'sell'  
                stock = -500
                pos = 2
            else:
                if pos == 1:
                    cash += 500*tradeprice
                    record.ix[j,symbol] = -500.0
                    record.ix[j,'adv'] = 'sell'  
                elif pos ==2:
                    cash -= 500*tradeprice
                    record.ix[j,symbol] = 500.0
                    record.ix[j,'adv'] = 'buy'  
                stock = 0
                pos = 0   

            df.ix[j, 'port_val'] = cash + stock*tradeprice

        #print(tradeprice)
        print df['port_val']
        print(record['adv'])
        print(tradeprice*500-initprice*500+sv)
        return record


    # def plottt(self,df,symb,sv):
    #     bench = self.addBench(df.copy(), symb, sv)
    #     df = df/df.ix[0]
    #     title = symb[0]+' hehe'
    #     ax = bench.plot(title=title, label=symb[0]+'_benchmark', color='black')
    #     df['port_val'].plot(color='green', label='portval_ML')
    #     plt.savefig(title)
    #     plt.show()

    def querystate(self, bbv, k, vol):
        state = 0
        bbv_cond=k_cond=vol_cond=True
        for i in range(1,self.bucket):

            if bbv_cond and bbv <= self.thresholds[i,0]:
                state += i*((self.bucket)**2)
                bbv_cond = False
        
            if vol_cond and vol <= self.thresholds[i,2]:
                state += i
                vol_cond = False
        
            if k_cond and k <= self.thresholds[i,2]:
                state += i*self.bucket
                k_cond = False

            if not (k_cond or bbv_cond or vol_cond):
                break

        return state



    def addthreshold(self, df, symb):
        temp = np.zeros((self.bucket, self.idct))

        bbv = np.sort(df['BBV'].values)
        #k = np.sort(df['k'].values)
        #k = np.sort(df['mom'].values)
        k = np.sort(df['ppo'].values)
        vol = np.sort(df['vol'].values)

        # dictstep = {0:1,1:3,2:7,3:9,4:10}
        # step = len(df)/10

        step = len(df) / self.bucket

        for i in range(self.bucket):
            temp[i,0] = bbv[(i+1)*step]
            temp[i, 1] = k[(i+1) * step]
            temp[i, 2] = vol[(i+1) * step]

        # for i in range(self.bucket):
        #     temp[i,0] = bbv[dictstep[i]*step]
        #     temp[i, 1] = k[dictstep[i] * step]
        #     temp[i, 2] = vol[dictstep[i] * step]

        self.thresholds = temp



    def addIndicators(self, df, symb):
        df = self.calc_bbv(df.copy(), symb)
        #df = self.calc_kdj(df.copy(),symb)
        df = self.calc_volatility(df.copy(),symb)
        #df = self.calc_mom(df.copy(),symb)
        df = self.calc_ppo(df.copy(),symb)
        return df

    def calc_mom(self, df,symb):
        mom = ((df[symb[0]] / df[symb[0]].shift(20))-1)[20:]
        df['mom'] = mom
        return df
        
    def calc_volatility(self,df, symb):
        dr = ((df[symb[0]] / df[symb[0]].shift(1))-1)[1:]
        vol = pd.rolling_std(dr, 20)    
        ma = vol.max()
        mi = vol.min()
        df['vol'] = (vol-mi)/(ma-mi)
        return df

    def calc_bbv(self,df, symb):
        rmean = pd.rolling_mean(df[symb[0]], window=20)
        rstd = pd.rolling_std(df[symb[0]], window=20)
        df['SMA'] = rmean
        df['RSTD'] = rstd
        df['BBV'] = (df[symb[0]]-df['SMA'])/(2*df['RSTD'])
        df.drop('SMA', axis=1, inplace=True)
        df.drop('RSTD', axis=1, inplace=True)
        return df

    def calc_ppo(self,df,symb):
        df['EMA26'] = pd.ewma(df[symb[0]],span=26)
        df['EMA9'] = pd.ewma(df[symb[0]],span=9)
        df['ppo'] = (df['EMA9']-df['EMA26'])/df['EMA26']
        df.drop('EMA26', axis=1, inplace=True)
        df.drop('EMA9', axis=1, inplace=True)
        return df

    def calc_kdj(self,df,symb):
    #Raw Stochastic Value
        df['mi'] = pd.rolling_min(df[symb[0]], window=14)
        df['ma'] = pd.rolling_max(df[symb[0]], window=14)
        df['k'] = (df[symb[0]]-df['mi'])/(df['ma']-df['mi'])
        #KDJ ----------- TODO:????????????ling hun tiao can
        #df['k'] = pd.rolling_mean(df['rsv'], window=3)
        #df['k'] = df['rsv']
        df['d'] = pd.rolling_mean(df['k'], window=3)
        df['j'] = 3*df['k']-2*df['d']
        df.drop('mi', axis=1, inplace=True)
        df.drop('ma', axis=1, inplace=True)
        df.drop('j', axis=1, inplace=True)
        return df
    


    def rubric(df, col):
        port_val = df[col]
        cr = port_val[-1]/port_val[0]-1
        ev = port_val[-1]
        dr = (port_val-port_val.shift(1))/port_val
        adr = dr.mean()
        sddr = dr.std()
        sr = (adr-rfr)/sddr*np.sqrt(sf)
        print("--------------------------------------")
        print(col)
        print('cr: '+str(cr))
        print('ev: '+str(ev))
        print('adr: '+str(adr))
        print('sddr: '+str(sddr))
        print('sr: '+str(sr))
        print("--------------------------------------")

