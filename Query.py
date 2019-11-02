# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 16:23:53 2019

@author: 13669
"""
import pickle
import codecs
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np
from datetime import date


class Account:
    
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
        df['Date']=pd.to_datetime(df['Date'],format='%Y-%m-%d')
        return df

    def monthselect(self,recorddf,y=date.today().year,m=date.today().month):
        df = recorddf
        df['Date']=pd.to_datetime(df['Date'],format='%Y-%m-%d')
        df2 = df.reset_index(drop=True)
        df2 = df.set_index('Date')
        y = str(y)
        m = str(m)
        y_m = y+'-'+m
        return df2[y_m]
    
    def DailyAccount(self,recorddf):
        df = pd.DataFrame(recorddf)
        df.sort_values(by='Date',inplace=True)  
        df2 = df.reset_index(drop=True)
        df2.set_index('Date')
        Ban = round(df['Amount'].sum(),2)
        print('Banlance: ${}'.format(Ban))
        return df2
  
      
class  SaveAccount(Account): 
    
    def getsave(self,recorddf):
        df = pd.DataFrame(recorddf)
        S = df[df['Amount'] > 0]
        Save = pd.DataFrame(data=S)
        return Save  
    
    def Journal(self,moneydatafile,savedf):   
        df = savedf
        df.sort_values(by='Date',inplace=True)
        print(df)
        S1 = df.groupby(by='Date')['Amount'].sum()
        S = pd.DataFrame(S1).reset_index()
        N = len(S)
        intd = np.arange(N)
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.plot(intd,abs(S['Amount']),'o-')
        ax.set_xticks(intd)
        pd.to_datetime(S['Date'],format='%Y-%m-%d')
        def format_date(x, pos=None):
            thisind = np.clip(int(x+0.5), 0, N-1)
            return S['Date'][thisind].strftime('%Y-%m-%d')
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
        fig.autofmt_xdate()
        plt.show()
        S['Amount'] = np.float64(S['Amount'])
        Ban = S['Amount'].sum()
        Ban2 = round(Ban,2)
        return('Total Save: ${}'.format(Ban2))
        
    def Classification(self,moneydatafile,savedf):
        df = savedf
        c = df.groupby(by='Class')['Amount'].sum()
        c1 = pd.DataFrame(c).reset_index()
        c1.sort_values(by='Amount',inplace=True,ascending=False)
        c1['Percent(%)'] = c1['Amount'].apply(lambda x :x*100/c1['Amount'].sum())
        c1['Percent(%)'] = round(c1['Percent(%)'],2)
        print(c1.reset_index(drop=True)) 
        sizes = list(abs(c1['Amount'].values))
        labels = c1['Class']
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes,labels = labels, autopct='%1.1f%%',shadow=True, startangle=90)
        ax1.axis('equal')
        plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
        plt.title('Cost pie Chart')
        return(plt.show())
        

class CostAccount(Account):
    
    def getcost(self,recorddf):
        df = pd.DataFrame(recorddf)
        C = df[df['Amount'] < 0]      
        Cost = pd.DataFrame(data=C)
        return Cost 
        
    def Journal(self,moneydatafile,costdf):   
        df = costdf
        df.sort_values(by='Date',inplace=True)
        print(df)
        C1 = df.groupby(by='Date')['Amount'].sum()
        C = pd.DataFrame(C1).reset_index()
        N = len(C)
        intd = np.arange(N)
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.plot(intd,abs(C['Amount']),'o-')
        ax.set_xticks(intd)
        def format_date(x, pos=None):
            thisind = np.clip(int(x+0.5), 0, N-1)
            return C['Date'][thisind].strftime('%Y-%m-%d')
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
        fig.autofmt_xdate()
        plt.show()
        C['Amount'] = np.float64(C['Amount'])
        Ban = C['Amount'].sum()
        Ban2 = round(Ban,2)
        return('Total Cost: $ {}'.format(Ban2))

    def Classification(self,moneydatafile,recorddf):
        df = self.getcost(recorddf)
        c = df.groupby(by='Class')['Amount'].sum()
        c1 = pd.DataFrame(c).reset_index()
        c1.sort_values(by='Amount',inplace=True,ascending=True)
        c1['Percent(%)'] = c1['Amount'].apply(lambda x :x*100/c1['Amount'].sum())
        c1['Percent(%)'] = round(c1['Percent(%)'],2)
        print(c1.reset_index(drop=True)) 
        sizes = list(abs(c1['Amount'].values))
        labels = c1['Class']
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes,labels = labels, autopct='%1.1f%%',shadow=True, startangle=90)
        ax1.axis('equal')
        plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
        plt.title('Cost pie Chart')
        return(plt.show())
        

