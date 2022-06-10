# Place N Queens in the Chess board(NXN) so that no queens can attack each other

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


def countNQueen(n,board,r):

    if r == n:
        # Print board
        for i in range(n):
            for j in range(n):
                print(board[i][j],end=" ")
            print()
        print()
        return 1


    ways = 0
    for c in range(n):
        if canPlace(board,n,r,c):
            board[r][c] = 1
            ways += countNQueen(n,board,r+1)
            board[r][c] = 0 # Backtrack

    return ways


if __name__=="__main__":
    
    for i in range(4,5):
        board = [[0 for i in range(20)] for j in range(20)]
        print("Solving for ",i,"queens. No of ways is",countNQueen(i,board,0))
        
