from secret import get_secret_key
from menu import menu, create, find, find_accounts

secret = get_secret_key()

if passw == secret:
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
