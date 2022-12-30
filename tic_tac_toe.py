'''
The purpose of this program is to play tic tac to against the computer. The computer places an O in a random position after the users input. 
Author: Baldeep Dhada
'''
import random

def load_map(map_file):
    '''
    Loads a map from a file as a grid (list of lists)
    '''
    with open(map_file, "r") as file:
        text = file.read()
        text_list = text.splitlines() 

        newlist = [] 
        for i in text_list:
                for j in i:
                    newlist.append(j)
        
        index = 0 
        final_list = [] 
        for i in range(0, len(text_list)):
                row = []
                for j in range(0, len(text_list[0])):
                        item = newlist[index]
                        index += 1
                        row.append(item)
                final_list.append(row)    
        
        return final_list

def starting_map():
    '''
    Displays the instructions and a map that will be used as a reference to play the game
    '''
    with open("starting_map.txt", "r") as file:
        text = file.read()   
    
    print(text)
        
def update_grid(grid, x_position):
    '''
    Updates the grid with an input from the User and a randomly selected position from the computer
    '''
        
    grid[x_position[0]][x_position[1]] = "X"
    
    new_list = []
    marker_list = [grid[0][0], grid[0][2], grid[0][4], grid[2][0], grid[2][2], grid[2][4], grid[4][0], grid[4][2], grid[4][4]] # all possible positions to place an X/O
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
                    # checks for positions in marker_list that don't have an X or O
                    if grid[i][j] != "X" and grid[i][j] != "O": 
                        if grid[i][j] in marker_list:
                            new_list.append([i, j])    
                            
    if len(new_list) != 0: # to avoid an error from using random on an empty list
        o_position = random.choice(new_list)
    
        grid[o_position[0]][o_position[1]] = "O"
    
    return grid

def display_map(updated_grid):
    """
    Displays the map.
    """       
    for row in updated_grid:
        a_row = ''
        for col in row:
                a_row += str(col) + ''
        print(a_row)
    
def get_command():
    '''
    Gets a command from the user
    '''
    command = input("Where do you want to position the X? Enter a number from 1-9: ")
    
    return command

def place_x(command):
    '''
    Takes the command and returns the corresponding position in the map
    '''
    if command == "1":
        return [0, 0]
    elif command == "2":
        return [0, 2]
    elif command == "3":
        return [0, 4]
    elif command == "4":
        return [2, 0]
    elif command == "5":
        return [2, 2]
    elif command == "6": 
        return [2, 4]
    elif command == "7":
        return [4, 0]
    elif command == "8":
        return [4, 2]
    elif command == "9":
        return [4, 4]
    else:
        print("Please enter a number from 1-9!")
        return False
        
def valid_position(updated_grid, x_position):
    """
    Checks if the user is placing an X in a position that doesn't have an X/O.
    """
    markers = ["X", "O"]
   
    if updated_grid[x_position[0]][x_position[1]] in markers:
        print("There is a marker in this position, please select another")
        return True
    else: 
        return False

def win(updated_grid):
    '''
    checks if the user has won or lost the game 
    '''

    win = [updated_grid[0][0], updated_grid[0][2], updated_grid[0][4]] # horizontal (first row)
    win2 = [updated_grid[2][0], updated_grid[2][2], updated_grid[2][4]] # horizontal (second row)
    win3 = [updated_grid[4][0], updated_grid[4][2], updated_grid[4][4]] # horizontal (third row)
    win4 = [updated_grid[0][0], updated_grid[2][0], updated_grid[4][0]] # vertical (first coloumn)
    win5 = [updated_grid[0][2], updated_grid[2][2], updated_grid[4][2]] # vertical (second coloumn)
    win6 = [updated_grid[0][4], updated_grid[2][4], updated_grid[4][4]] # vertical (third coloumn)
    win7 = [updated_grid[0][0], updated_grid[2][2], updated_grid[4][4]] # diagonal (left to right)
    win8 = [updated_grid[0][4], updated_grid[2][2], updated_grid[4][0]] # diagonal (right to left)
    
    win_list = [win, win2, win3, win4, win5, win6, win7, win8]  
    
    for i in range(len(win_list)):
        if win_list[i].count("X") == 3:
            print("Congratulations! You won the game!")
            return True
        elif win_list[i].count("O") == 3:
            print("You lost to the opponent!")
            return True
        else: 
            continue

def main():
    starting_map()
    grid = load_map("map_tictacto.txt")
    a = True
    # get the correct input the first time so the grid can be updated
    while a == True:
        command = get_command()
        x_position = place_x(command)
        if x_position != False:
            updated_grid = update_grid(grid, x_position)
            display_map(updated_grid)
            a = False
        
    winning = True 
    turns = 0
    while winning == True:
        command = get_command()
        x_position = place_x(command)
        if x_position != False:
            if valid_position(updated_grid, x_position) == False:
                updated_grid = update_grid(grid, x_position)
                display_map(updated_grid)
                if win(updated_grid) == True:
                    break
                # if the turn limit is hit and the user doesn't win or lose the game
                turns += 1
                if turns == 4 and win(updated_grid) != True:
                    print("Its a draw!")
                    winning = False
        
if __name__ == '__main__':
    main()