# https://codeforces.com/gym/100886/problem/G
# Maximum Product of Digits

def product(n):

    ans = 1
    while(n):
        ans *= n%10
        n //= 10
    return ans


def maxProd():
    bstr = str(b)

    ans = b
    for i in range(len(bstr)):

        if bstr[i] == '0':
            continue

        curr = list(bstr)
        curr[i] = str(int(bstr[i])-1)

        for j in range(i+1, len(bstr)):
            curr[j] = '9'
        
        curr_num = int("".join(curr))
        if curr_num >= a and product(ans) < product(curr_num):
            ans = curr_num
    return ans


def findMax(pos, ta, tb, st):
    
    if pos == len(astr):
        return (1, "")

    start = int(astr[pos]) if ta else 0
    end = int(bstr[pos]) if tb else 9

    ans = -1
    s = []

    for i in range(start, end+1):

        val = i
        if st == 0 and i == 0:
            val = 1

        if (pos,ta,tb,st) in memo:
            return memo[pos,ta,tb,st]
        temp = findMax(pos+1, ta & (i == start), tb & (i == end), st | i > 0)
        if temp[0] * val > ans:
            ans = temp[0]*val

            if i == 0 and st == 0:
                s = temp[1]
            else:
                s = temp[1]+str(i)

    memo[pos,ta,tb,st] = (ans,s)
    return (ans, s)


def maxProd1():
    global astr, bstr, memo
    astr = str(a)
    bstr = str(b)

    while len(astr) < len(bstr):
        astr = '0'+astr

    memo = {}
    ans = findMax(0,1,1,0)
    return (ans[0], ans[1][::-1])

if __name__ == "__main__":
    a = 1
    b = 10
    print(maxProd())
    print(maxProd1())

    a = 51
    b = 62
    print(maxProd())
    print(maxProd1())