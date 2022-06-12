
def fib_memo(n):
    global count
    global memo

    count += 1
    if n <= 2:
        return n
    if memo[n] != -1:
        return memo[n]
    
    memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]

def fib_tab(n):

    tab = [0 for i in range(n+1)]
    tab[1] = 1
    tab[2] = 2
    for i in range(3,n+1):
        tab[i] = tab[i-1] + tab[i-2]
    return tab[n]

if __name__ == "__main__":

    count = 0
    memo = [-1 for i in range(20+1)]
    print(fib_memo(20), count)
    print(fib_tab(20))