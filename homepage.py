# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 18:36:21 2021

@author: bshpa
"""

#homepage for user to picks options

def main():
    print("Welcome to Password Manager, pick an option below: \na) Generate a password \nb) Get password for account\nc) Create new password")
    while True:
        user_choice=input("Enter your choice (a, b, or c): ")
        if user_choice=='a':
            #generate password
            #use password for a new account
            break
        if user_choice=='b':
            #get password for an account
            break
        if user_choice=='c':
            #store password for a new account
            break
        else:
            print("Invalid input, please try again")

main()