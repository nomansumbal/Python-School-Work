#=============================================================
#Program:       Payroll Program
#Programmer:    Noman Sumbal
#Date:          4/12/2022
#Abstract:      Processes worker information by using the 
#               worker class file, which processes and returns
#               the workers pay.
#==============================================================

import Workers

def main():
    #List of employees and volunteers
    worker_list = create_list()

    print("These are the workers and their ID numbers, city, shift, and pay: ")
    print("------------------------------------------------------------------")

    show_list(worker_list)

def create_list():
    #Initialize list of workers
    worker_list =[]

    #Volunteer worker info
    print("Please enter in the information for the volunteer")
    name = input('\nWhat is the volunteers name? ')
    id_number = input(f"What is {name.title()}'s ID-Number? ")
    city = input(f"What city is {name.title()} from? ")
    
    #We must pass the volunteer workers information into the Worker class file, so we append the Volunteer as an Object with attributes in the list
    volunteer_worker = Workers.Person(name, id_number, city)
    worker_list.append(volunteer_worker)

    #Hourly Worker info
    print("\nNow put in the information for 3 hourly workers.")
    
    for worker in range(1, 4):
        name = input("What is the employee's name? ")
        id_number = input(f"What is {name.title()}'s Employee number? ")
        city = input(f"What city is {name.title()} in? ")
        shift = input(f"What shift does {name.title()} work? ")

        #checks if the type of shift entered is correct
        while shift != '1' and shift != '2' and shift != '3':
            print("ERROR: The shift can only be 1, 2, or 3")
            shift = input(f"Please enter the correct shift that {name.title()} works. ")
        
        pay_rate = float(input(f"What is {name.title()}'s Pay Rate? "))

        #Create a hourly worker object with information that was given as input
        hourlyworker = Workers.HourlyWorker(name, id_number, city, shift, pay_rate)
        worker_list.append(hourlyworker)

    #Salary Worker info
    print("\nPlease enter the information for the Salary Worker. ")
    name = input("What is the salary workers name? ")
    id_number = input(f"Please enter the ID Number for {name.title()}. ")
    city = input(f"Please enter the city that {name.title()} is from. ")
    pay_rate = float(input(f"Please enter the annaul salary for {name.title()}. "))

    #Creates a salary worker object with information that was given as an input
    salary_worker = Workers.SalaryWorker(name, id_number, city, pay_rate)
    worker_list.append(salary_worker)

    worker_list.append("Invalid Object")

    return worker_list

def show_list(worker_list):
    for worker in worker_list:
        if isinstance(worker, Workers.Person):
            worker.employee_info()
            worker.show_pay()
        else:
            print("ERROR: This doesn't seem to be a valid object.")

main()
input("Press any key to exit the program.")
