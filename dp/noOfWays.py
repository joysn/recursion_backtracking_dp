# number of ways we can reach n by using 1, 2 and 3
# f(1) = 1
# f(2) = [1,1], [2] = 2
# f(3) = [1,1,1],[1,2],[2,1],[3] = 4
# f(4) = f(n-1) + f(n-2) + f(n-3)

def noOfWays(n):
    if n <= 2:
        return n
    if n == 3:
        return 4

    ways = [0 for i in range(n+1)]
    ways[1] = 1
    ways[2] = 2
    ways[3] = 4

    for i in range(4,n+1):
        ways[i] = ways[i-1]+ways[i-2]+ways[i-2]
    return ways[-1]

if __name__=="__main__":
    for i in range(6):
        print(noOfWays(i))