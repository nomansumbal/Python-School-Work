#===========================================================================
#Program: Record / DvD Sale Program
#Programmer: Noman Sumbal
#Date: 3/28/2022
#Abstract: This program processes the payment due after reading a file by 
#          processing the code associated with the CD or Record
#===========================================================================

#Constant variables that won't change
CD_PRICE = 16.5
DVD_PRICE = 21.75


def main():
    #Counter Intialization
    cd_customer_counter = 0
    dvd_customer_counter = 0
    total_payment_due = 0

    #Printing Column Headings
    print("Customer Name \tCode\tSpindle\tPayment Due")
    print('')

    #Exception handler for file
    try:
        #opens file that will be processed
        infile = open("disks.txt", 'r')

        #Read's first line as customer name
        customer_name = infile.readline()

        #While field is NOT empty continues to process file
        while customer_name != '':

            #Strips new line from customer name then prints it
            customer_name = customer_name.rstrip('\n')
            print(customer_name, end = '\t')

            #Reads code, strips new line, and then prints it
            code = infile.readline()
            code = code.rstrip('\n')
            print(code, end = '\t')

            #Reads spindle field, strips new line, and then prints it
            spindles = infile.readline()
            spindles = int(spindles)
            print(spindles, end = '\t')

            #Calculates appropriate payment according to the code
            if code.lower() == 'c':
                payment_due = spindles * CD_PRICE
                cd_customer_counter += 1
            elif code.lower() == 'd':
                payment_due = spindles * DVD_PRICE
                dvd_customer_counter += 1
            else:
                payment_due = 0
            
            #Sums up total payment
            total_payment_due += payment_due

            #Invalid code message
            if payment_due == 0:
                print("Invalid Code")
            else:
                print('$', payment_due)
            
            #Reads next line as customer name to go through the loop again
            customer_name = infile.readline()

        #closes file
        infile.close()

        #Displays number of Cd's and DvD's purchased and Total of all payments
        print('')
        print(f"Total number of customers that purchased CD-RW's: {cd_customer_counter}")
        print(f"Total number of customers that purchased DVD-RW's: {dvd_customer_counter}")
        print('')
        print(f"Total of payments due: ${total_payment_due}")

    #Exception block
    except IOError:
        print("Error trying to open or read disks.txt")

    
main()
input()
