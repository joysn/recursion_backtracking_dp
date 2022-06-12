
def binaryStringCount(idx):
    global count
    count += 1
    if idx == 0:
        return 1
    if idx == 1:
        return 2

    if memo[idx] != -1:
        return memo[idx]
    memo[idx] = binaryStringCount(idx-1) + binaryStringCount(idx-2)
    return memo[idx]

def binaryStringCountTab(idx):
    global n
    tab = [0 for i in range(n+1)]
    
    tab[0] = 1
    tab[1] = 2
    for i in range(2,n+1):
        tab[i] = tab[i-1] + tab[i-2]
    return tab[idx]

if __name__ == "__main__":

    for n in range(2,11):
        count = 0
        memo = [-1 for i in range(n+1)]
        
        print(binaryStringCount(n))
        # print(count)
        print(binaryStringCountTab(n))