#function to generate next iteration of the pattern
def new_gen(board, board_size):                     
        #newboard is at the beginning full of dead cells
	newboard = []
	for i in range(board_size):
		row = []
		for j in range(board_size):
			x = '□'
			row.append(x)
		newboard.append(row)
        #for each cell in row put dead cell in, then put all rows in newboard
		
	height = len(board)

	#for each cell in current board, we count the number of its live neighbors
	#i is the number of rows, j is number of collums
	for i in range(len(board)):
		width = len(board[i])
		for j in range(len(board[i])): 
			live_count = 0
			if i-1 >= 0 and j-1>= 0 and board[i-1][j-1] ==	'■':
				live_count += 1
			if i-1 >= 0 and board[i-1][j] == '■':
				live_count += 1
			if i-1 >= 0 and j+1 < width and board[i-1][j+1] ==	'■':
				live_count += 1
			if j+1 < width and board[i][j+1] == '■':
				live_count += 1
			if i+1 < height and j+1 < width and board[i+1][j+1] == '■':
				live_count += 1
			if i+1 < height and board[i+1][j] == '■':
				live_count += 1
			if i+1 < height and j-1 >= 0 and board[i+1][j-1] ==	'■':
				live_count += 1
			if j-1 >=0 and board[i][j-1] ==	'■':
				live_count += 1
				
			#here we apply the rules of the Game of Life and map the new cells into newboard	
			if live_count < 2 and board[i][j] == '■':
				newboard[i][j] = '□'
			elif (live_count == 2 or live_count == 3) and board[i][j] == '■':
				newboard[i][j] = '■'
			elif live_count > 3 and board[i][j] == '■':
				newboard[i][j] = '□'
			elif live_count == 3 and board[i][j] == '□':
				newboard[i][j] = '■'
	
	return newboard


def printboard(board):
        for i in range(len(board)):
                print(" ".join(board[i]))
	
#function that opens the excel document so no need to use 'if, else' many times
def get_file_name(argument):
    file_cases = {
        'a' : 'acorn.csv',
	'b' : 'beacon.csv',
	'c' : 'block_witch_engine.csv',
	'd' : 'boat.csv',
	'e' : 'diehard.csv',
	'f' : 'glider.csv',
	'g' : 'glider_gun.csv',
	'h' : 'r_pentomino.csv',
	'i' : 'spaceship.csv',
	'j' : 'unbounded.csv'
    }
    return file_cases.get(argument, "Invalid letter")
#-------------------------------------------------
import time
import os
from random import randint

#the user has 2 choices, either to have a board with dead and live cells randomly arranged
#or to choose from patterns

random_or_choice = input("Enter 1 for random or 2 to choose pattern: ")
while not random_or_choice =="1" and not random_or_choice =="2":
        print("Wrong input")
        random_or_choice = input("Enter 1 for random or 2 to choose pattern: ")

#the user can decide how big the board will be
board_size = int(input("Enter the board size: "))
while board_size < 0:
        print("Wrong input")
        board_size = int(input("Enter the board size: "))

my_board = [board_size * ['□'] for i in range(board_size)]

if random_or_choice == "1":
        for i in range(board_size):
                        for j in range(board_size):
                                choice = randint(0,1)  #here the cells have a 50% chance of being dead or alive
                                if choice == 1:
                                        my_board [i][j] = '■'
                                else:
                                        my_board[i][j] = '□'
                                        

elif random_or_choice == "2":

        list_of_patterns = ['a','b','c','d','e','f','g','h','i','j']

        print('List of  patterns: ')
        print('\n')
        print(' a: acorn')
        print(' b: beacon')
        print(' c: block_witch_engine')
        print(' e: diehard')
        print(' f: glider')
        print(' g: glider_gun')
        print(' h: r_pentomino')
        print(' i: spaceship')
        print(' j: unbounded')

        users_choice = input('Enter the pattern letter from the list above to load the pattern: \n')

        while not users_choice in list_of_patterns:
                print("Wrong input. Use letters a-j")
                users_choice = input('Enter the pattern letter to load the pattern: \n')

                
#this opens the excel file and puts the pattern into the board
        f=open(get_file_name(users_choice), "r") #r = read_only
        if f.mode == 'r':
                contents =f.read()
                rows = contents.splitlines()
                height_of_pattern = len(rows)
                width_of_pattern = len(rows[0].split(','))
                pattern = []
	
                for i in range(height_of_pattern):
                        pattern.append(rows[i].split(','))

#because the pattern is not a square we need to operate with the side that is bigger
#(to be able to fit it properly into the board)
                if height_of_pattern > width_of_pattern:
                        size = height_of_pattern
                else:
                        size = width_of_pattern
                
#each pattern has a different size
#the user needs to make a board that is as big as the pattern or bigger to see it work
                while board_size < size:
                        print("Pattern size is too big for board")
                        board_size = int(input("Enter the board size: "))

                my_board = [board_size * ['□'] for i in range(board_size)]

#to put the pattern in the middle of the board
                
                x_offset = int((board_size - len(pattern[0]))/2)
                y_offset = int((board_size - len(pattern))/2)
                for i in range(len(pattern)):
                        for j in range(len(pattern[i])):
                                if pattern[i][j] == '1':
                                        my_board[i+ y_offset ][j+ x_offset] = '■'
                                else:
                                        my_board[i+y_offset][j+x_offset] = '□'

               
                
                
print("prvni generace")
printboard(my_board)
print()
	
iterations = int(input('Enter the number of iterations: \n'))

while iterations < 0:
        print("Wrong input")
        board_size = int(input("Enter the number of iterations: \n"))
        
for i in range(int(iterations)):
        my_board = new_gen(my_board, board_size)
        time.sleep(0.5)
        os.system("cls")
        printboard(my_board)
		
	
