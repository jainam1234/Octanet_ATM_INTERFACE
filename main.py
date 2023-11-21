import getpass
import string
import os

# creating lists of users, their PINs, and bank statements
users = ['jainam', 'jd', 'doshi']
pins = ['1234', '2222', '3333']
amounts = [1000, 2000, 3000]
count = 0

# while loop checks existence of the entered username
print("****************************************************************************")
print("*                                                                          *")
print("*                         Welcome to ATM MACHINE                           *")
print("*                                                                          *")
print("****************************************************************************")
while True:
    user = input('\nENTER USER NAME: ')
    user = user.lower()
    if user in users:
        n = users.index(user)
        break
    else:
        print('----------------')
        print('INVALID USERNAME')
        print('----------------')

# comparing pin
while count < 3:
    print('------------------')
    pin = input('PLEASE ENTER PIN: ')
    print('------------------')
    if pin.isdigit():
        if pin == pins[n]:
            break
        else:
            count += 1
            print('-----------')
            print('INVALID PIN')
            print('-----------')
            print()
    else:
        print('------------------------')
        print('PIN CONSISTS OF 4 DIGITS')
        print('------------------------')
        count += 1

# in case of a valid pin - continuing, or exiting
if count == 3:
    print('-----------------------------------')
    print('3 UNSUCCESSFUL PIN ATTEMPTS, EXITING')
    print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
    print('-----------------------------------')
    exit()

print('-------------------------')
print('LOGIN SUCCESSFUL, CONTINUE')
print('-------------------------')
print()
print('--------------------------')
print(str.capitalize(users[n]), 'welcome to ATM')
print('----------ATM SYSTEM-----------')

while True:
    print('-------------------------------')
    response = input(
        'SELECT FROM FOLLOWING OPTIONS: \nTransaction History__(T) \nWithdraw___(W) \nDeposit__(D)  \nTransfer___(Tf) \nQuit_______(Q) \nType The Letter Of Your Choices: ').lower()

    print('-------------------------------')
    valid_responses = ['t', 'w', 'd', 'tf', 'p', 'q']
    response = response.lower()

    if response == 't':
        print('---------------------------------------------')
        print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n], 'RUPEES ON YOUR ACCOUNT.')
        print('---------------------------------------------')

    elif response == 'w':
        print('---------------------------------------------')
        cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
        print('---------------------------------------------')
        if cash_out % 10 != 0:
            print('------------------------------------------------------')
            print('AMOUNT YOU WANT TO WITHDRAW MUST MATCH 10 RUPEES NOTES')
            print('------------------------------------------------------')
        elif cash_out > amounts[n]:
            print('-----------------------------')
            print('YOU HAVE INSUFFICIENT BALANCE')
            print('-----------------------------')
        else:
            amounts[n] = amounts[n] - cash_out
            print('-----------------------------------')
            print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
            print('-----------------------------------')

    elif response == 'd':
        print()
        print('---------------------------------------------')
        cash_in = int(input('ENTER AMOUNT YOU WANT TO DEPOSIT: '))
        print('---------------------------------------------')
        print()
        if cash_in % 10 != 0:
            print('----------------------------------------------------')
            print('AMOUNT YOU WANT TO LODGE MUST MATCH 10 RUPEES NOTES')
            print('----------------------------------------------------')
        else:
            amounts[n] = amounts[n] + cash_in
            print('----------------------------------------')
            print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
            print('----------------------------------------')

    elif response == 'tf':
        print('---------------------------------------------')
        transfer_user = input('ENTER USERNAME TO TRANSFER TO: ').lower()
        if transfer_user in users:
            transfer_amount = int(input('ENTER AMOUNT TO TRANSFER: '))
            if transfer_amount <= amounts[n]:
                transfer_index = users.index(transfer_user)
                amounts[n] -= transfer_amount
                amounts[transfer_index] += transfer_amount
                print('---------------------------------------------')
                print('TRANSFER SUCCESSFUL')
                print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
                print('---------------------------------------------')
            else:
                print('-----------------------------')
                print('YOU HAVE INSUFFICIENT BALANCE')
                print('-----------------------------')
        else:
            print('--------------------------')
            print('INVALID TRANSFER USERNAME')
            print('--------------------------')

    elif response == 'q':
        exit()

    else:
        print('------------------')
        print('RESPONSE NOT VALID')
        print('------------------')
