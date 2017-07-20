# -*- coding: utf-8 -*-

import pandas as pd
import time, sys, os, csv, datetime
import numpy as np

os.chdir('../volDatabase')

path = str(sys.argv[1])

Date = time.mktime(datetime.datetime.strptime(path,'%Y%m%d').timetuple())

Data = pd.read_csv(path, header=None, skiprows=1)
Data.columns=['Portfolio','ATMVol','Skew','ATMBid','ATMAsk','Downside1','Downside2','Upside1','Upside2']

Data['micro_time_stamp'] = Date

Data = Data[['micro_time_stamp','Portfolio','ATMVol','Skew','ATMBid','ATMAsk','Downside1','Downside2','Upside1','Upside2']]

Data.to_csv('../VolCurveParams_'+path,index=False)
