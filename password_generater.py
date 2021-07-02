import string
import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!@#$%^&*()<>{}?+_"

x = string.uppercase_letters + string.lowercase_letters + string.digits + string.symbols


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

amount = 15

for x in range(amount):
    password = ''.join([random.choice(x) for _ in range(amount)])    
    print(password)
