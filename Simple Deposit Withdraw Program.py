#================================================================
# Program:       ATM Program
# Programmer:    Noman Sumbal
# Date:          2/3/2022
# Abstract:      This program is a simulation of an ATM.
#                It will process deposits, withdrawals,
#                and invalid transaction codes, and provide
#                a current balance.
#=================================================================

#The main function
def main():

    name = input("what is your name? ")
    account_ID = input("What is your account ID? ")
    transaction_code = input("Enter W or w for Withdrawal, Press D or d for Desposit ")
    previous_balance = float(input("What is your previous balance? "))
    transaction_amount = float(input("How much is the transaction amount? "))

    if transaction_code == "w" or transaction_code == "W":
        withdraw_process(previous_balance, transaction_amount)

    elif transaction_code == "d" or transaction_code == "D":
        deposit_process(previous_balance, transaction_amount)

    else:
        invalid_code(previous_balance)

#Process Deposit Function
def deposit_process(previous_balance, transaction_amount):

    new_balance = transaction_amount + previous_balance
    display_function(new_balance)


#Withdrawal Function
def withdraw_process(previous_balance, transaction_amount):

    if previous_balance >= transaction_amount:
        new_balance = previous_balance - transaction_amount

    else:
        print("Invalid Transaction: Not Enough Funds!")
        new_balance = previous_balance

    display_function(new_balance)

#Error if user enters in a code rather than D or W
def invalid_code(previous_balance):
    new_balance = previous_balance

    print("Invalid Transaction Code: ")
    print("Type W or w for withdrawal")
    print("Type D or d for deposit")

    display_function(new_balance)

def display_function(new_balance):
    print("Your balance is now $", format(new_balance, '.2f'))

#calls main function after initializing program
main()

input("Press enter to exist the program!")