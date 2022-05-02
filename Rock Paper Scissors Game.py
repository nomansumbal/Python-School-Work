#===========================================================================
#Program: Rock Paper Scissors
#Programmer: Noman Sumbal
#Date: 3/21/2022
#Abstract: This program takes a players choice and compares it to a random
#          computer choice and displays the winner of the game
#===========================================================================

import random

#main program logic
def main():
    play_again = 'y'
    number_of_tied_games = 0
    number_of_player_wins = 0
    number_of_computer_wins = 0

    print("Let's play a game of Rock, Paper, Scissors")
    while play_again == 'y' or play_again == 'Y':

        #get's computer and players choice
        computer_choice = process_computer_choice()
        player_choice = process_player_choice()

        #display's computer choice
        if computer_choice == 1:
            print("Computer chooses Rock.")
        elif computer_choice == 2:
            print("Computer chooses Paper.")
        elif computer_choice == 3:
            print("Computer chooses Scissors.")

        #displays players choice
        if player_choice == 1:
            print("You chose Rock.")
        elif player_choice == 2:
            print("You chose Paper.")
        elif player_choice == 3:
            print("You chose Scissors.")
        
        #Get's result of game and updates game scores
        winner = determine_winnner(player_choice, computer_choice)
        if winner == 'computer':
            number_of_computer_wins += 1
        elif winner == 'player':
            number_of_player_wins += 1
        else:
            number_of_tied_games += 1
        
        play_again = input('Do you want to play again? Enter y for yes: ')
        
    print(f"There were {number_of_tied_games} games tied.")
    print(f"The Computer won {number_of_computer_wins} games.")
    print(f"You won {number_of_player_wins} games.")

#gets computers choice
def process_computer_choice():
    computer_choice = random.randint(1,3)

    return computer_choice

#gets players choice
def process_player_choice():
    player_choice = float(input("What is your choice? Enter 1 for rock, 2 for paper, or 3 for scissors: "))
    
    #checks if input is correct
    while player_choice != 1 and player_choice != 2 and player_choice != 3:
        print("ERROR: your choice can only be 1,2, or 3.")
        player_choice = float(input("Please enter a correct choice: "))
    
    return player_choice

#Logic to determine the winner
def determine_winnner(player_choice, computer_choice):
    if computer_choice == 1:
        if player_choice == 2:
            print("Paper beats Rock, You win!")
            winner = 'player'
        elif player_choice == 3:
            print("Rock beats Scissors, the Computer wins!")
            winner = 'computer'
        else:
            print("The game is tied, try again.")
            winner = 'tied'

    if computer_choice == 2:
        if player_choice == 1:
            print("Paper beats Rock, Computer wins!")
            winner = 'computer'
        elif player_choice == 3:
            print("Scissors beats Paper, You wins!")
            winner = 'player'
        else:
            print("The game is tied, try again.")
            winner = 'tied'

    if computer_choice == 3:
        if player_choice == 1:
            print("Rock beats Scissors, You win!")
            winner = 'player'
        elif player_choice == 2:
            print("Scissors beats Paper, the Computer wins!")
            winner = 'computer'
        else:
            print("The game is tied, try again.")
            winner = 'tied'
    return winner

main()
input("Press any key to exit!" )
