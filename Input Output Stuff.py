#======================================================================
#Program: Convert
#Programmer: Noman Sumbal
#Date: 1/28/2022
#Abstract:This program converts the number of gallons entered
#         to its equivalent in quarts and liters which are
#         displayed as output.
#======================================================================

#get input from user
gallons = int(input('How many gallons? '))

#do the conversions
quarts = gallons * 4
liters = gallons * 3.785

#display the output to the user
print('The number of quarts in', gallons, ' gallons is', quarts)
print('The number of liters in', gallons, ' gallons is', liters)

input('Press enter to exit!')
