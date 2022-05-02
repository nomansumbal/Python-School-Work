#=============================================================
# Program:      Homework 3
# Programmer:   Noman Sumbal
# Date:         2/2/2022
# Abstract:     This program uses functions to calculate pay,
#               gross pay, witholding and net pay
#
#=============================================================

def main():
    display_message()

    #Get name
    employee_name = input("Enter employee's name: ")

    #Get sales
    sales_amount = float(input("Enter the sales amount: "))

    #Get Hours
    hours_worked = int(input("Enter hours worked by this employee: "))

    #Calculate Hourly Pay
    hourly_pay = hours_worked * hourly_pay_rate

    #Calculate Commission
    commission = sales_amount * commission_rate

    #Caculate Gross Pay
    gross_pay = hourly_pay + commission

    #Caculate Witholding
    withholding = gross_pay * withholding_rate

    #Calculate net pay
    net_pay = gross_pay - withholding
    display_results(hourly_pay, commission, gross_pay, withholding, net_pay)

def display_message():
    print("This program caculate the salesperson's pay.")
    print("Five values are display:")
    print("hourly pay, commission, gross pay, withholding, and net pay.")
    print("")

def display_results(hourly_pay, commission, gross_pay, withholding, net_pay):
    print("The hourly pay amount is: %.2f" % hourly_pay)
    print("The commission amount is: %.2f" % commission)
    print("The gross pay amount is: %.2f" % gross_pay)
    print("The withholding amount is: %.2f" % withholding)
    print("The net pay amount is: %.2f" % net_pay)

hourly_pay_rate = float(7.50)
commission_rate = float(0.05)
withholding_rate = float(0.25)
main()

input("Press Enter to exit!")
