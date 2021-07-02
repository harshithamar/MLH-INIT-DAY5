from .secrets import key
from menu import menu, create, find, find_accounts

secret = key()

if passw == secrets:
    print('You\ are in')

else:
    print('Bad Luck')
    exit()

choice = menu()

while choice != 'Q':
    if choice == '1':
        create()
    if choice == '2':
        find_accounts()
    if choice == '3':
        find()
    else:
        choice = menu()

exit()
