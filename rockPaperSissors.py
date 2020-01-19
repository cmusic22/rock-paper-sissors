"""
Capstone Project 1 Spring 2020
Rock, Paper, Sissors

In this game the user will be asked to select
Rock Paper or Sissors, the computer will do the
same and a winner will be announced.

"""
#import random functions
import random 
#main function
def main():
	#welcome message
	print("Welcome to Rock, Paper, Sissors")
	#get computers choice
	compChoice = get_compChoice()
	print("Computer made its choice")
	#get user choice
	userChoice = get_userChoice()
	print (userChoice)
	#get winner
	winner = get_winner(compChoice, userChoice)
	#display choices & winner, or announce tie
	#if tie automatic replay, if not ask if they want to play again
	print(winner)

#dictonary
rps = {
	"rock": 1,
	"paper": 2,
	"sissors": 3
}

#functions
#fuction for computers choice
def get_compChoice():
	cC = random.randrange(1, 4, 1)
	return cC

#user choice
def get_userChoice():
	uC = input('Choose rock, paper, or sissors: ').lower()
	del rps[uC]
	return rps

#winner
def get_winner(cC, uC):
	if cC == 1 and uC == 1:
		winner = 'Tie, Rock!'
	elif cC == 1 and uC == 2:
		winner = 'You win with Paper!'
	elif cC == 1 and uC == 3:
		winner = 'Computer wins with Rock!'
	elif cC == 2 and uC == 1:
		winner = 'Computer wins with Paper!'
	elif cC == 2 and uC == 2:
		winner = 'Tie, Paper!'
	elif cC == 2 and uC == 3:
		winner = 'You win with Sissors!'
	elif cC == 3 and uC == 1:
		winner = 'You win with Rock!'
	elif cC == 3 and uC == 2:
		winner = 'Computer winns with Sissors!'
	elif cC == 3 and uC == 3:
		winner = 'Tie, Sissors!'
	return winner

main()


