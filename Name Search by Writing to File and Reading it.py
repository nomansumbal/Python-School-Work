#=================================================================================
#Program:       Names Using List Variables
#Programmer:    Noman Sumbal
#Date:          4/3/2022
#Abstract:      Creating list variables and outputting a sequential data file
#================================================================================


def main():
    #List get's stored in Name variable
    names = get_names()

    #outputs all the names in the list
    print("Unsorted list of names: ", end = '\n')
    output_names(names)

    #sorts the list of names
    names.sort()

    #Outputs sorted list of names
    print("Sorted list of names: ", end = '\n')
    output_names(names)

    #writes list to new file
    copyname(names)

    #User can search through the list of names
    search_names(names)


def get_names():
    #opens the file, reads the data, then returns data to the main function
    infile = open('names.txt', 'r')

    #Reads lines and stores them in a list
    names = infile.readlines()
    infile.close()
    namecounter = 0

    #Iterates through list and removes newline \n from string
    while namecounter < len(names):
        names[namecounter] = names[namecounter].rstrip('\n')
        namecounter += 1
    
    #returns list to main function
    return names


def output_names(names):
    for i in names:
        print(i)

def copyname(names):
    #copies original list of names and input it into new file
    secondary_names = names
    outfile = open('newnames.txt', 'w')

    #puts each name in the list into the new file on unique lines
    for i in secondary_names:
        outfile.write(i + '\n')
    outfile.close()

def search_names(names):

    search = 'y'
    while search.lower() == 'y':
        name = input('Who would you like to search for? ')

        if name in names:
            print(f'{name} was found in the list')
            spot = names.index(name)
            print(f'The name {name} is found at index {spot}')
        else:
            print(f'{name} was not found in the list')
        search = input('Do you want to search the list again? (y/n): ')

main()
input('Press any key to exit the program.')