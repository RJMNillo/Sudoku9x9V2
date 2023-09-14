from Sudoku9x9 import Sudoku9x9


if __name__ == '__main__':
    print("Amogus")
    SudokuInstance = Sudoku9x9()
    squareAvailability = SudokuInstance.createBlock()
    SudokuInstance.printSquare()