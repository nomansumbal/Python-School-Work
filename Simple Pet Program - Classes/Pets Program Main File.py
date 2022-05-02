#==============================================
#Program:       Processing pet data
#Programmer:    Noman Sumbal
#Date:          4/10/2022
#Abstract:      get's and displays data from the
#               Pet class
#===============================================

import Pets

def main():
    pets = create_list()

    print("Here's the pet data: ")
    show_list(pets)    

def create_list():
    
    pet_list = []

    print("Please enter the data for three unique pets")
    for i in range(1, 4):
        print(f'Pet number {i}')
        pet_name = input("Enter you pet's name: ")
        pet_type = input("Enter the type of pet: ")
        pet_age = input("Enter the pet's age: ")
        print('')

        pet = Pets.PetData(pet_name, pet_type, pet_age)

        pet_list.append(pet)

    return pet_list

def show_list(PetList):

    for animal in PetList:
        print(f"Pet's name is: {animal.get_pet_name()}")
        print(f"Pet's type is: {animal.get_pet_type()}")
        print(f"Pet's age is: {str(animal.get_pet_age())}")
        print("")

main()
input('Press any key to exit.')