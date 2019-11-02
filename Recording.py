# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 09:55:52 2019

@author: 13669
"""
from datetime import datetime,date
import pickle

class Recording:
 
    cla_cost={'1':'Housing','2':'Clothing','3':'Food','4':'Learning','5':'Internet',
     '6':'Pet','7':'Sports','8':'Medical','9':'Travel','10':'Snacks','11':'entertainment',
     '12':'Gift','13':'Digital Product','14':'Transportation'}
    cla_save={'1':'Part-time','2':'Salary','3':'Bonus','4':'Else'}
    
    def _init_(self):
        self.amount = 0
        self.classification = 0
        
    def Save(self,moneydatafile,recordtxtfile,amount,Class,Comment):    #Recording save
        Date = self.Date()
        self.amount = float(amount)
        comment = Comment
        #print('Classification: ',Recording.cla_save)
        c = int(Class)
        self.classification = Recording.cla_save[str(c)]
        with open(moneydatafile,'rb') as mm:
             self.balance = pickle.load(mm) + self.amount
        with open(moneydatafile,'wb') as mm:
             pickle.dump(self.balance,mm)
        with open(recordtxtfile,'a') as mr:
             mr.write('%-15s%-10s%-10s%-20s\n' % (Date,self.amount,self.classification,comment))
        with open(moneydatafile,'rb') as mm: 
              balance = pickle.load(mm)
              print("Latest Balance:$ %d" % balance)
    
    def Cost(self,moneydatafile,recordtxtfile,amount,Class,Comment):    #Recording cost
        Date = self.Date()
        self.amount = -(float(amount))
        comment = Comment   
        #print('Classification: ',Recording.cla_cost)
        c = int(Class)
        self.classification = Recording.cla_cost[str(c)]
        with open(moneydatafile,'rb') as mm: 
             self.balance = pickle.load(mm) + self.amount
        with open(moneydatafile,'wb') as mm:
             pickle.dump(self.balance,mm)   
        with open(recordtxtfile,'a') as mr: 
             mr.write('%-15s%-10s%-10s%-20s\n' % (Date,self.amount,self.classification,comment))
        with open(moneydatafile,'rb') as mm: 
              balance = pickle.load(mm)
              print("Latest Balance:$ %d" % balance)
              
    def Date(self):
        a = int(input('Do you want to record save or cost for today? (Today:1,Other:2) \n'))
        if a == 1:
            dt = date.today()
            Date = dt.strftime('%Y-%m-%d')
            return Date
        elif a == 2:
            year = int(input('Year: \n'))
            month = int(input('Month: \n'))
            day = int(input('Day: \n'))
            Date = datetime(year,month,day)
            Date = Date.strftime('%Y-%m-%d')
            return Date
        else:
            print('Invalid Input! Try Again.')
            
