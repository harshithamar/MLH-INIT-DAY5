# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 18:59:53 2021

@author: bshpa
"""

#this file will help access passwords
import numpy as np

def access():
    f2=open("passwords.txt","r")
    
    print("Which account's password would you like to access? ")
    
    #file_content stores every line in file
    #accounts stores the account names
    file_content=np.zeros(4)
    accounts=[]
    #i is used as a counter to help collect user input
    i=0
    
    for line in f2:
        i=i+1
        file_content=line.split()
        accounts=accounts+[file_content[0]]
        print(str(i)+". "+str(accounts[i-1]))
    
    f2.close()
    
    f3=open("passwords.txt","r")
        
    #collecting user input after printing options
    user_account=int(input("Enter number: "))
    #j is another counter that will keep getting incremented until we find the user's choice
    j=0
    #data stores the account information
    data=np.zeros(4)
    for line in f3:
        j=j+1
        #when we get a match:
        if int(j)==user_account:
            data=line.split()
            print("Account: "+str(data[0]))
            print("Email id: "+str(data[1]))
            print("Username: "+str(data[2]))
            print("Password: "+str(data[3]))
        
    