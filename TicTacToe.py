import random

print("Welcome to Tic Tac Toe. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.  ")


# generates the array grid
def genGrid():
    grid = []
    for row in range(3):
        grid.append([' ']*3)
    return grid

# outputs a given array grid with column and row headers
def printGrid(grid):
    colNumbers = "  "
    for colNum in range(3):
        colNumbers += str(colNum + 1) + "   "
    print(colNumbers)
    for index,row in enumerate(grid):
        rowOutput = str(index + 1) + " "
        for cellNum,cell in enumerate(row):
            rowOutput += cell + " | "
        print(rowOutput)

# Get and execute players next move
def userMove(grid):
    while True:
        try:
            userturn = input("Enter your next position <x,y>: ")
            userturn = userturn.split(',')
            pickX = int(userturn[1])
            pickY = int(userturn[0])
            if not (pickX > 0 and pickX <= 3) and (pickY > 0 and pickY <= 3):
                print("MAX co-ordinate value is " + str(3))
            elif grid[pickX - 1][pickY - 1] != " ":
                print("That position is already occupied!")
            else:
                break
        except:
            print("Both co-ordinates must be integers: x,y")
            
    grid[pickX - 1][pickY - 1] = "X"
    return pickX, pickY

# Check every win possibility
def winCheck(grid, player):
    return (
        (grid[0][0] == player and grid[1][0] == player and grid[2][0] == player) or # across the top
        (grid[0][1] == player and grid[1][1] == player and grid[2][1] == player) or # across the middle
        (grid[0][2] == player and grid[1][2] == player and grid[2][2] == player) or # across the bottom

        (grid[0][0] == player and grid[0][1] == player and grid[0][2] == player) or # down the left side
        (grid[1][0] == player and grid[1][1] == player and grid[1][2] == player) or # down the middle
        (grid[2][0] == player and grid[2][1] == player and grid[2][2] == player) or # down the right side

        (grid[0][0] == player and grid[1][1] == player and grid[2][2] == player) or # diagonal
        (grid[2][0] == player and grid[1][1] == player and grid[0][2] == player) # diagonal
    )

# duplicate given 2D array grid
def copyGrid(grid):
    copy = []
    for index,row in enumerate(grid):
        copy.append([])
        for cell in row:
            copy[index].append(cell)
    return copy

def noviceMove(grid):
    # Check if Computer can win this go...
    # (adds every possible move to a duplicate grid, and checks if an AI win occurs)
    for rowNum in range(0,3):
        for cellNum in range(0,3):
            copy = copyGrid(grid)
            if copy[rowNum][cellNum] == " ":
                copy[rowNum][cellNum] = "O"
                if winCheck(copy, "O"):
                    return rowNum, cellNum

    possibleMoves = []
    if grid[1][0] == " ":
         possibleMoves.append([1,0])
    elif grid[2][1] == " ":
        possibleMoves.append([2,1])
    elif grid[1][2] == " ":
        possibleMoves.append([1,2])
    elif grid[0][1] == " ":
        possibleMoves.append([0,1])

    if len(possibleMoves) > 0:
        move = random.choice(possibleMoves)
        return move[0], move[1]

    # No moves available
    return None


def expertMove(grid):
    # Check if Computer can win this go...
    # (adds every possible move to a duplicate grid, and checks if an AI win occurs)
    for rowNum in range(0,3):
        for cellNum in range(0,3):
            copy = copyGrid(grid)
            if copy[rowNum][cellNum] == " ":
                copy[rowNum][cellNum] = "O"
                if winCheck(copy, "O"):
                    return rowNum, cellNum

    # Block the player if they can win next go...
    # (adds every possible move to a duplicate grid, and checks if a player win occurs)
    for rowNum in range(0,3):
        for cellNum in range(0,3):
            copy = copyGrid(grid)
            if copy[rowNum][cellNum] == " ":
                copy[rowNum][cellNum] = "X"
                if winCheck(copy, "X"):
                    return rowNum, cellNum

    # Try and go in a random corner
    possibleMoves = []
    if grid[0][0] == " ":
        possibleMoves.append([0,0])
    if grid[2][0] == " ":
        possibleMoves.append([2,0])
    if grid[0][2] == " ":
        possibleMoves.append([0,2])
    if grid[2][2] == " ":
        possibleMoves.append([2,2])

    if len(possibleMoves) > 0:
        move = random.choice(possibleMoves)
        return move[0], move[1]

    # Try go to center of grid
    if grid[1][1] == " ":
        return 1,1

    # Go to a random side
    possibleMoves = []
    if grid[1][0] == " ":
        possibleMoves.append([1,0])
    elif grid[2][1] == " ":
        possibleMoves.append([2,1])
    elif grid[1][2] == " ":
        possibleMoves.append([1,2])
    elif grid[0][1] == " ":
        possibleMoves.append([0,1])

    if len(possibleMoves) > 0:
        move = random.choice(possibleMoves)
        return move[0], move[1]

    # No moves available
    return None

if __name__ == "__main__":
    # Initial generation & output of the grid
    grid = genGrid()
    printGrid(grid)

    count = 0 # Incrementing counter to ensure no more than 9 moves are played
    while not winCheck(grid, "X") and not winCheck(grid, "O"):  # loops until either player or AI wins
        if count >= 9:  # exit loop if 9 moves have been played ('>' as a failsafe)
            break
        count += 1
        print("\n")

        # get user input, add to grid and output new grid...
        userMove(grid)
        printGrid(grid)


        if not winCheck(grid, "X"):     # if the player didn't win from their previous go
            if count >= 9:  # exit loop if 9 moves have been played ('>' as a failsafe)
                break
            count += 1
            print("\n")

            print("Computers turn")
            aiRow, aiCol = expertMove(grid)     # calculate and store best next move
            grid[aiRow][aiCol] = "O"    # make move by setting grid value
            printGrid(grid)     # output new grid
        else:
            break       # player won from their previous go

    if winCheck(grid, "X"):
        print("Congrats, You Win!")
    elif winCheck(grid, "O"):
        print("The Computer Wins!!")
    else:
        print("It's a Draw!!")
