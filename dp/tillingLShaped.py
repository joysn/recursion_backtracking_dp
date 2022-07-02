# Tilling 2XN board with 1X2, 2X1 and L Shaped Tile

# f(n) is number of ways n*n board can be tiled
# g*n) is number of ways n*n board with one additional square at the top row can be tiled
# h(n) is number of ways n*n board with one additional square at the bottom row can be tiled
# f(n) = f(n-1) + f(n-2) + g(n-2) + h(n-2)
# g(n) = h(n)
# f(n) = f(n-1) + f(n-2) + 2*g(n-2)
# g(n) = h(n-1) + f(n-1)
# g(n) = g(n-1) + f(n-1)

def countTiles(n):

    f = [0 for i in range(n+1)]
    g = [0 for j in range(n+1)]
    f[0] = g[0] = 0
    f[1] = g[1] = 1
    f[2] = g[2] = 2
    print(f,g)
    for i in range(3,n+1):
        f[i] = f[i-1] + f[i-2] + 2*g[i-2]
        g[i] = g[i-1] + f[i-1]

    return f[-1]

if __name__ == "__main__":
    n = 10
    print(countTiles(n))