#====================================================================================
#Program:       Main Class Person (Volunteer), Hourly Worker, and Salary Worker
#Programmer:    Noman Sumbal
#Date:          4/12/2022
#Abstract:      This program is what stores and keeps data about the workers.
#               It can also calculate pay rates for the workers.
#===================================================================================

SHIFT2_PREMIUM = 0.5
SHIFT3_PREMIUM = 0.10
PAY_PERIODS = 26
 
#Volunteer worker, only gets paid in love.
class Person:

    #Initializes Person's Attributes. Since this is the Parent class its attributes will be inherited
    #by other classes that get pass through it
    def __init__(self, name, id_number, city):
        self.__name = name
        self.__id_number = id_number
        self.__city = city
    
    #Sets person's name
    def set_name(self,name):
        self.__name = name
    
    #Sets person's id number
    def set_id_number(self, id_number):
        self.__id_number = id_number

    #Sets person's city
    def set_city(self, city):
        self.__city = city
    
    #Returns person's name, ID number, or city to function that called it
    def get_name(self):
        return self.__name
    
    def get_id_number(self):
        return self.__id_number
    
    def get_city(self):
        return self.__city
    
    #This function gives the employees Name, ID number, and City
    def employee_info(self):
        print(f"This Employee's name is {self.__name}")
        print(f"This Employee's ID-Number is {self.__id_number}")
        print(f"This Employee's city is {self.__city}")

    #How much money the volunteer makes. Spoiler - it's nothing but love
    def show_pay(self):
        print('-----------------------------------------------')
        print("This person is a volunteer so they aren't paid")
        print('-----------------------------------------------\n')
    
class HourlyWorker(Person):

    #This intializes the Hourly Worker class, with all the attributes a Volunteer has
    #The unique attributes are 'shift' and 'pay_rate'
    def __init__(self, name, id_number, city, shift, pay_rate):
        Person.__init__(self, name, id_number, city)
        self.__shift = shift
        self.__pay_rate = pay_rate
        
    #Calculates the employees payment and prints it out.
    def show_pay(self):
        print(f"Employee's shift is: {self.__shift}")

        #Gives specific rate depending on shift type
        if self.__shift == '1':
            premium_rate = self.__pay_rate

        elif self.__shift == '2':
            premium_rate = (SHIFT2_PREMIUM * self.__pay_rate) + self.__pay_rate

        else:
            premium_rate = (SHIFT3_PREMIUM * self.__pay_rate) + self.__pay_rate

        print(f"The employee's hourly rate is ${premium_rate}\n")

#Works on set salary       
class SalaryWorker(Person):

    def __init__(self, name, id_number, city, pay_rate):
        Person.__init__(self, name, id_number, city)
        self.__pay_rate = pay_rate
    
    def show_pay(self):
        print(f"Employee's annual salary is ${self.__pay_rate}")
        biweeky_salary = float(self.__pay_rate) / PAY_PERIODS
        print(f"The employee's bi-weekly pay is ${biweeky_salary}\n")