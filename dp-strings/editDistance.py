# Edit Distance


def editDistance(i,j):

    if i == len(s1) and j == len(s2):
        return 0
    elif i == len(s1):
        return len(s2) - j
    elif j == len(s2):
        return len(s1) - i

    # i < len(s1) and j < len(s2)
    if (i,j) in memo:
        return memo[(i,j)]
    ans = 0
    if s1[i] != s2[j]:
        ans = 1 + min(editDistance(i+1,j), editDistance(i,j+1), editDistance(i+1,j+1))
    else:
        ans = editDistance(i+1,j+1)

    memo[(i,j)] = ans
    return ans


def editDistanceBU():

    cache = [[0 for col in range(len(s1)+1)] for row in range(len(s2)+1)]

    for col in range(1,len(s1)+1):
        cache[0][col] = col

    for row in range(1, len(s2)+1):
        cache[row][0] = row

    for row in range(1, len(s2)+1):
        for col in range(1, len(s1)+1):
            if s1[col-1] != s2[row-1]:
                cache[row][col] = 1 + min(cache[row-1][col-1], cache[row-1][col], cache[row][col-1])
            else:
                cache[row][col] = cache[row-1][col-1]
    # print(cache)
    return cache[len(s2)][len(s1)]
    

if __name__ == "__main__":

    s1 = "FOOD"
    s2 = "MONEY"

    memo = {}
    print(editDistance(0,0))
    print(editDistanceBU())

    s1 = "FOOD"
    s2 = "FOO"
    memo = {}
    print(editDistance(0,0))
    print(editDistanceBU())

    s1 = "FOOD"
    s2 = "FOODS"
    memo = {}
    print(editDistance(0,0))
    print(editDistanceBU())


    s1 = "FOOD"
    s2 = "XXFOOD"
    memo = {}
    print(editDistance(0,0))
    print(editDistanceBU())