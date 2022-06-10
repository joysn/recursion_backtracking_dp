# Solve Sudoku and return one solution

def canPlace(board, r, c, num, n):
    
    # Check the row
    for curr_c in range(n):
        if board[r][curr_c] == num:
            return False
    
    # Check the column
    for curr_r in range(n):
        if board[curr_r][c] == num:
            return False
    
    # Check the subgrid
    for row in range(int(r/3)*3,int(r/3)*3+3):
        for col in range(int(c/3)*3,int(c/3)*3+3):
            if board[row][col] == num:
                return False
    
    return True

def solveSudoku(board,r,c,n):
    
    # Base case
    if r == n:
        for i in range(n):
            for j in range(n):
                print(board[i][j],end=" ")
            print()
        print()
        return True

    # End of Row
    if c == n:
        return solveSudoku(board, r+1,0,n)
    
    # Prefilled Cell
    if board[r][c] != 0:
        return solveSudoku(board, r,c+1,n)

    # Cell to be filled
    for num in range(1,10):
        if canPlace(board,r,c,num,n):
            board[r][c] = num
            success = solveSudoku(board,r,c+1,n)
            if success:
                return True
    # If no option works
    board[r][c] = 0 #Backtracking
    return False


if __name__=="__main__":

    board = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]
    
    solveSudoku(board,0,0,9)
        
