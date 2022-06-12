def countSetBitsTab(n):
    count = [0 for i in range(n+1)]

    for i in range(1,n+1):
        count[i] = count[int(i/2)] + i%2
        print(count[i])
    

if __name__ == "__main__":

    n = 20
    countSetBitsTab(n)
    