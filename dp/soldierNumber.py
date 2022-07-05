# https://codeforces.com/problemset/problem/546/D
# Soldier and Number Game
# Reference - https://www.geeksforgeeks.org/prime-factorization-using-sieve-olog-n-multiple-queries/
# Reference - https://codeforces.com/blog/entry/18034

import math
# get the prime factors for all # from 2 to 5000000
def sieve():
    spf[1] = 1
    # Initialized with the number itself
    for i in range(2,maxnum+1):
        spf[i] = i
    
    # Set 2 for every even number
    for i in range(4, maxnum+1,2):
        spf[i] = 2

    # set for rest
    for i in range(3, math.ceil(math.sqrt(maxnum))):
        # not yet set
        if spf[i] == i:
            for j in range(i*i, maxnum+1,i):
                if spf[j] == j:
                    spf[j] = i

def getPrimeCount(n):
    if n == 1:
        return 0
    cnt = 1+ getPrimeCount(n//spf[n])
    return cnt

def maxScore():
    maxscore = 0
    for i in range(b+1,a+1):
        maxscore += getPrimeCount(i)
    
    return maxscore

if __name__== "__main__":
    maxnum = 5000000
    maxnum = 50
    spf = [0 for i in range(maxnum+1)]
    sieve()
    # print(spf)
    a = 3
    b = 1
    # target = math.factorial(a)//math.factorial(b)
    print(maxScore())
    # for i in range(1,13):
    #     print(getPrimeCount(i))

    a = 6
    b = 3
    print(maxScore())
