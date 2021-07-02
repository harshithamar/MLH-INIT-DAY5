import string
import random

def generator(amount):
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "!@#$%^&*()<>{}?+_"
    
    x = uppercase_letters + lowercase_letters + digits + symbols
    
    
    upper, lower, nums, symb = True, True, True, True
    
    password = ""
    
    all = ""
    
    if upper:
        all = uppercase_letters
    if lower:
        all = lowercase_letters
    if nums:
        all = digits
    if symb:
        all = symbols
    
    password = ''.join((random.choice(x) for i in range(amount)))    
    return password


