#================================================================================
# Program:          Average Sale Calculator
# Programmer:       Noman Sumbal
# Date:             2/4/2022
# Abstract:         This program will input a salesperson's name followed by the
#                   first sale amount and then the number of sales as indicated
#                   below for a used car dealership. The program will then display
#                   the salesperson's average, highest, and lowest sale.
#=================================================================================

#The main function
def main():
     
    # Initializes condition that runs the while loop
    keep_going = "y"

    # Counter for the sales person
    number_of_salesperson = 0

     # While loop which processes each persons sales
    while keep_going == "y" or keep_going == "Y":
         
        #function that processess the salesperson
        process_sale()

        number_of_salesperson += 1

        keep_going = input("Are there any sales person's? Enter Y for Yes and N for No: ")

    print(f"There were {number_of_salesperson} salespersons processed." )


def process_sale():
    
    #Get's Sales Persons name
    name = input("Enter salesperson's name: ")

    #Asks for the number of sales name has mande.
    print(f"Enter {name}'s amount for the first sale: ", end="")
    first_sale = float(input())

    while first_sale < 1 or first_sale > 25000:

        #Asks user to enter a correct sale amount
        print("")
        print("ERROR: First sale can't be less than $1 or greater than $25000")
        first_sale = float(input("Please enter a correct sale amount: "))
    
    #declaring variables that will be used
    total_sales = first_sale
    highest_sale = first_sale
    lowest_sale = first_sale
    

    #Asks how many sales the person has
    print(f"How many sales does {name} have? ", end = "")
    number_of_sales = int(input())

    #If number of sales is greater than 1 then the for loop will not be able to compare and close program
    if number_of_sales > 1:
        # Loop which compares the sales and finds lowest, highest, and average sales
        for number in range(2, number_of_sales + 1):

            #asks for sale amount
            print(f"Enter {name}'s sale #{number}: ", end = "")
            sale = float(input())

            #Checks whether or not the sale is less than 1 or greater than 25000
            while sale < 1 or sale > 25000:
                print("")
                print("ERROR: The sale cannot be less than 1 or greater than 25000")
                sale = float(input("Please enter a correct sale amount: "))

            # Sums up all the sales
            total_sales += sale

            #Make's sure the correct sale is the highest sale
            if sale > highest_sale:
                highest_sale = sale
        
            #Make's sure the correct sale is the lowest one
            elif sale < lowest_sale:
                lowest_sale = sale
        
            #Calculates the average sale
            average_sale = float(total_sales) / number_of_sales

        #Displays average, highest, and lowest sales
        print("")
        print(f"{name}'s average sale was: ${average_sale}")
        print(f"{name}'s highest sale was: ${highest_sale}")
        print(f"{name}'s lowest sale was: ${lowest_sale}")
        print("")
    else:
        print("")
        print(f"{name} only had one sale. It was ${first_sale}")
        print("")

#Calls the main function
main()

input("Press enter to exit the program!")