from Sudoku9x9 import Sudoku9x9

class Sudoku9x9Solver():
    def __init__(self, square = None):
        self.square = Sudoku9x9(square)
        # Basically just that, really

    # Helper Functions
    # checkEmpty: check if there are empty squares
    def checkEmpty(self):
        print("The current state of our square is: ")
        self.square.printSquare()
        isEmpty = False
        for row in range(0, len(self.square.square)):
            if 0 in self.square.square[row]:
                isEmpty = True
        if isEmpty:
            print("There are still empty spots in the table.")
        else:
            print("You have filled the table. GG")
        return isEmpty
    
    # checkBlocked: check if there are any squares blocked
    def checkBlocked(self):
        print("The current space available for our squares are: ")
        space = self.square.createBlock()

        # Print the space
        for row in range(0, len(space)):
            print(space[row])
        
        # Go through the rows and check if there are zeroes
        hasZero = False

        for row in range(0, len(space)):
            if 0 in space[row]:
                hasZero = True
        
        if hasZero:
            print("We are blocked! Removing a number...")
        else:
            print("We are still in relative clarity.")
        
        return hasZero


    