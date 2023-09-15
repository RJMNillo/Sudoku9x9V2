import random

empty9x9Square = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

availableNumberIndex = [1,2,3,4,5,6,7,8,9]

class Sudoku9x9():
    # 
    def __init__(self, square = None):
        if square == None:
            self.square = empty9x9Square
        # This is when you want to put in another 9x9 square of your choosing
        else:
            self.square = square
        
        # This part will be using a for loop to put in the available number index
        # Might be long, but it will be useful for my implementation
        self.availabilitylistmatrix = []
        for row in range(0, len(self.square)):
            rowmatrix = []
            for col in range(0, len(self.square[row])):
                rowmatrix.append(availableNumberIndex)
            self.availabilitylistmatrix.append(rowmatrix)
    
    # Helper functions
    # printSquare: prints the square
    # createBlock: prints availability matrices's lengths and checks if any one 
    # insertNumber: Inserts the number in the given coordinates
    # removeNumber: Sets number in given coordinates to 0
    # ATTENTION: functions will be based on (row, col), as it is based on the for loops.
    def printSquare(self):
        for row in range(0, len(self.square)):
            print(self.square[row])
    
    def createBlock(self):
        availabilityLengths = []
        for row in range(0, len(self.square)):
            rowmatrix = []
            for col in range(0,len(self.square[row])):
                # If the square is empty, put in the length of the 
                if self.square[row][col] == 0:
                    rowmatrix.append(len(self.availabilitylistmatrix[row][col]))
                else:
                    rowmatrix.append(-1)
            availabilityLengths.append(rowmatrix)
        return availabilityLengths

    def insertNumber(self, y, x, number):
        self.square[y][x] = number
    
    def removeNumber(self, y, x):
        self.square[y][x] = 0