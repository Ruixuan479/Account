# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 20:57:05 2019

@author: 13669
"""
import numpy as np
import pandas as pd
import codecs
import pickle

class Modify:
    
    def _init_(self):
        pass
    
    def getdf(self,recordtxtfile):
        df = pd.DataFrame(columns = ['Date','Amount','Class','Comment'])
        Class = []
        Amount = []
        Date = []
        Com = []
        r = codecs.open(recordtxtfile, mode='r',encoding='utf-8')
        line = r.readline()
        while line:
            a = line.split()
            b = a[1]  
            c = a[2]
            d = a[0]
            Co = a[-1]          
            Amount.append(b)
            Class.append(c)
            Date.append(d)
            Com.append(Co)
            line =r.readline()
        r.close()
        df['Amount'] = np.float64(Amount)
        df['Class'] = Class
        df['Date'] = Date
        df['Comment'] = Com
        return df
    
    def DailyAccount(self,recorddf):
        df = pd.DataFrame(recorddf)
        df.sort_values(by='Date',inplace=True)  
        df2 = df.reset_index(drop=True)
        Ban = round(df2['Amount'].sum(),2)
        print('Banlance: ${}'.format(Ban))
        return df2
    
    def modify(self,moneydatafile,recordtxtfile,a,b,c):
        data = self.getdf(recordtxtfile)
        data2 = self.DailyAccount(data)
        df = pd.DataFrame(data2)
        a = int(a)
        b = int(b)
        if not (b == 2)|(b == 1)|(b == 0)|(b == 3):
            print('Invalid input. Try again.')
        elif (b == 2) | (b == 3) :
            m = str(c)
        elif b == 1 :
            m = np.float64(c)
            with open(moneydatafile,'rb') as mm:
                 balance = pickle.load(mm) + m - df.iloc[a,b]
            with open(moneydatafile,'wb') as mm:
                 pickle.dump(balance,mm)
        elif b == 0:
            #dt = datetime.strptime(c,"%Y-%m-%d")
            #m = dt.date()
            m = str(c)
        df.iloc[a,b] = m
        df.reset_index(drop=True)
        df.to_csv(recordtxtfile, sep='\t',index=False, header=False)
        return(self.DailyAccount(df))
            
class delete(Modify):
        
    def delete(self,moneydatafile,recordtxtfile,b):
        df = self.getdf(recordtxtfile)
        print(df)
        df2 = pd.DataFrame(df)
        with open(moneydatafile,'rb') as mm:
                 balance = pickle.load(mm) - df2.iloc[b][1]
        with open(moneydatafile,'wb') as mm:
                 pickle.dump(balance,mm)
        df2.drop(b,inplace=True)
        df2.reset_index(drop=True)
        df2.to_csv(recordtxtfile, sep='\t',index=False, header=False)
        return(self.DailyAccount(df2))
        