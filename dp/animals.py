# https://codeforces.com/problemset/problem/35/D
# 


def maxAnimals(cday,balFood):

    if cday > days:
        return 0
    

    if (cday,balFood) in memo:
        return memo[cday][balFood]
    ans = 0
    if animals[cday]*(days-cday+1) <= balFood:
        ans = max(ans, 1 + maxAnimals(cday+1,balFood-animals[cday]*(days-cday+1)))
    ans = max(ans, maxAnimals(cday+1,balFood))

    memo[cday,balFood] = ans
    return ans
    
if __name__== "__main__":
    days = 3
    food = 4
    animals = [0,1,1,1]
    memo = {}
    print(maxAnimals(1,food))
    # for i in range(days+1):
    #     animals[i] = animals[i]*(days-i+1)
    # print(animals)
    # print(maxAnimalsTab())



    days = 3
    food = 6
    animals = [0,1,1,1]
    memo = {}
    print(maxAnimals(1,food))

    days = 3
    food = 1
    animals = [0,1,1,2]
    memo = {}
    print(maxAnimals(1,food))