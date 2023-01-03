import random as rd

sudoku =[
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_sudoku(sudoku):
    for row in sudoku: 
        index_in_row = 0
        index_row = sudoku.index(row)
        if  index_row % 3 == 0 and index_row != 0: 
            print('- - - - - - ')
        for number in row:
            if index_in_row % 3 == 0 and index_in_row != 0:
                print('|', end ='')
            print(number, end= '')
            index_in_row +=1
            if index_in_row == len(row):
                print()

def find_zero(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i,j)

    return None

def check_row_col(sudoku, position, z):
    for j in range(len(sudoku[0])):
        if sudoku[position[0]][j] == z and j != position[1]:
            return False
        
    for i in range(len(sudoku)):
        if sudoku[i][position[1]] == z and i != position[0]:
            return False
    
    box_x = pos[0] // 3
    box_y = pos[1] // 3
    for x in range(box_x*3, box_x + 3):
        for y in range(box_y*3, box_y + 3):
            
            
    return True



def main(sudoku):
    
    position = find_zero(sudoku)
    if not position: 
        return True
    else: 
        row, col = position
    
    for z in range(1,10):
        if check_row_col(sudoku, (row, col), z):
            sudoku[row][col] = z

            if main(sudoku): #BACKTRACKING: prüft, ob main == True, 
                return True
            sudoku[row][col] = 0
    


    return False   

    


main(sudoku)
print_sudoku(sudoku)