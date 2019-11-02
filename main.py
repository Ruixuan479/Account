# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 15:47:49 2019

@author: 13669
"""
import os
import pickle
from Recording import Recording
from Query import Account,SaveAccount,CostAccount
from Modify import Modify,delete

modification = Modify()
Account = Account()
Record = Recording()
SaveAccount = SaveAccount()
CostAccount = CostAccount()
Modify = Modify()
Delete = delete()

def show_AccountingAssistant():
        mymoney= 'mymoney.data'
        myrecord = 'myrecord.txt'
        cla_save={'1':'Part-time','2':'Salary','3':'Bonus','4':'Else'}
        cla_cost={'1':'Housing','2':'Clothing','3':'Food','4':'Learning','5':'Internet',
     '6':'Pet','7':'Sports','8':'Medical','9':'Travel','10':'Snacks','11':'entertainment',
     '12':'Gift','13':'Digital Product','14':'Transportation'}
        if not os.path.exists(mymoney):
               with open(mymoney,'wb') as mm: 
                    pickle.dump(0,mm)

        prompt = """
(0)Record:
   Please enter 0 ^_^
(1)Query:
   Please enter 1 ^_^
(2)Modify:
   Please enter 2 ^_^
(3)Exit:
   please enter 3 ^_^.
Please input your choice(0/1/2/3): 
"""
        
        while True:
               record = Account.getdf(myrecord)
               try:
                    choice = input(prompt).strip()[0]   
               except ImportError:
                    continue
               except (KeyboardInterrupt,EOFError):
                    print()
                    choice == '3'
    
               if choice not in '0123':
                    print('Invalid input. Try again.')
                    continue
               if choice == '0':
                    a = input('Record save(0) or cost(1)? Input your choice: \n')
                    if a == '0':
                        print('Classification: ',cla_save)
                        amount = input('Amount:\n')
                        Class = input('Classification:\n')
                        Comment = input('Comment:\n')
                        print(Record.Save(mymoney,myrecord,amount,Class,Comment))
                    elif a== '1':
                        print('Classification: ',cla_cost)
                        amount = input('Amount:\n')
                        Class = input('Classification:\n')
                        Comment = input('Comment:\n')
                        Record.Cost(mymoney,myrecord,amount,Class,Comment)
               if choice == '1':
                    x = input('Query whole recordings(0) or just for one month(1)?\n')
                    if x == '0':
                        record = record
                    elif x == '1':
                        y = int(input('which year you want to query?(example:2011)\n'))
                        m = int(input('which month you want to query?(example:9)\n'))
                        record = Account.monthselect(record,y,m)
                        
                    a = input('Query Daily Account(0) or Save Account(1) or Cost Account(2)? Input your choice: \n')
                    if (a == '0') & (x == '1'):
                        df2 = Account.DailyAccount(record)
                        print(df2)
                    elif (a == '0') & (x == '0'):
                        df2 = Account.DailyAccount(record)
                        print(df2)
                    elif a == '1':
                        df_save = SaveAccount.getsave(record)
                        Journal_save = SaveAccount.Journal(mymoney,df_save)
                        print(Journal_save)
                        Classification_save = SaveAccount.Classification(mymoney,df_save)
                        print(Classification_save)                       
                    elif a == '2':
                        df_cost = CostAccount.getcost(record)
                        Journal_cost = CostAccount.Journal(mymoney,df_cost)
                        print(Journal_cost)
                        Classification_cost = CostAccount.Classification(mymoney,df_cost)
                        print(Classification_cost)                       
               if choice == '2':
                    print(Account.DailyAccount(record))
                    a = input('Delete a record(0) or modify(1) Input your choice:?\n')
                    if a == '0':     
                        b = int(input('Which record do you want to delete (index starts from 0):\n'))
                        print(Delete.delete(mymoney,myrecord,b)) ## you can change para to modify what you want
                    elif a == '1':
                        b = input('Row:\n')
                        c = input('Column:\n')
                        d = input('Modify to:\n')
                        print(Modify.modify(mymoney,myrecord,b,c,d)) ## you can change para to modify what you want
               if choice == '3':
                    break              

if __name__ == '__main__':
    show_AccountingAssistant()