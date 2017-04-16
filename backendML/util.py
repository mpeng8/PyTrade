
import quandl 
import pandas as pd
from datetime import datetime, timedelta


def get_quandl(sd, ed, symb,db='WIKI/'):

    quandl.ApiConfig.api_key = "v9Yjy1pW7Ez_HkYqZZqz"
    mydata = quandl.get(db+symb, start_date=sd, end_date=ed)
    return mydata

def minusdate(datestr):
    ls = datestr.split('-')
    daya = datetime(int(ls[0]), int(ls[1]), int(ls[2]))
    delta = timedelta(days=34)
    res = daya-delta
    rt = str(res.year) + '-' + str(res.month) + '-' + str(res.day)
    return rt