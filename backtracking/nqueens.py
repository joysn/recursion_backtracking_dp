# Place N Queens in the Chess board(NXN) so that no queens can attack each other

global count
def canPlace(board,n,r,c):

    # Check for column
    for i in range(r):
        if board[i][c] == 1:
            return False
    i = r
    j = c
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    i = r
    j = c
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    return True


def solveNQueen(n,board,r):
    # Base case
    if r == n:
        # Print board
        for i in range(n):
            for j in range(n):
                print(board[i][j],end=" ")
            print()
        count += 1
        return True
    # Recursive Case
    # Will try to place a queen in every row
    for c in range(n):
        # current r,c is safe or not
        if canPlace(board,n,r,c):
            board[r][c] = 1
            possible = solveNQueen(n,board,r+1)
            if possible:
                return True
            board[r][c] = 0 # Backtrack
    return False
    


if __name__=="__main__":
    
    for i in range(6):
        board = [[0 for i in range(20)] for j in range(20)]
        print("Solving for ",i,"queens")
        if not solveNQueen(i,board,0):
            print("Cannot be solved")
        
