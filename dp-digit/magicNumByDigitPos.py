# https://codeforces.com/problemset/problem/628/D
# Magic Numbers

# Consider the decimal presentation of an integer. Let's call a number d-magic if digit d appears in decimal presentation 
# of the number on even positions and nowhere else.

# For example, the numbers 1727374, 17, 1 are 7-magic but 77, 7, 123, 34, 71 are not 7-magic. On the other hand the number 
# 7 is 0-magic, 123 is 2-magic, 34 is 4-magic and 71 is 1-magic.
# Find the number of d-magic numbers in the segment [a, b] that are multiple of m. Because the answer can be very huge you 
# should only find its value modulo 109 + 7 (so you should find the remainder after dividing by 109 + 7).
# Input
# The first line contains two integers m, d (1 ≤ m ≤ 2000, 0 ≤ d ≤ 9) — the parameters from the problem statement.
# The second line contains positive integer a in decimal presentation (without leading zeroes).
# The third line contains positive integer b in decimal presentation (without leading zeroes).
# It is guaranteed that a ≤ b, the number of digits in a and b are the same and don't exceed 2000.
# Output
# Print the only integer a — the remainder after dividing by 109 + 7 of the number of d-magic numbers in segment [a, b] that 
# are multiple of m.

def countM(idx,last,num_mod):
    if idx == n:
        return num_mod == 0

    if (idx,last,num_mod) in memo:
        return memo[idx,last,num_mod]
    ans = 0
    if idx%2 == 1:
        # Even position
        if last:
            if d <= int(s[idx]):
                ans += countM(idx+1,True,int(num_mod*10+d)%m)
        else:
            ans += countM(idx+1,False,(num_mod*10+d)%m)
    else:
        # odd position
        if last:
            for i in range(int(s[idx])+1):
                if i != d:
                    if i == int(s[idx]):
                        ans += countM(idx+1,True,int(num_mod*10+i)%m)
                    else:
                        ans += countM(idx+1,False,int(num_mod*10+i)%m)
        else:
            for i in range(10):
                if i != d:
                    ans += countM(idx+1,False,(num_mod*10+i)%m)

    memo[idx,last,num_mod] = ans
    return ans
    

def countMagicNum(_s):
    global s
    global n
    global memo
    s = _s
    n = len(s)
    memo = {}
    return countM(0,True,0)

def reduce(a):
    alist = list(a)
    for i in range(len(alist)-1,-1,-1):
        if alist[i] == '0':
            alist[i] = "9"
        else:
            alist[i] = str(int(alist[i]) - 1)
            break
    a = "".join(alist)
    return a

if __name__=="__main__":

    m = 2 
    d = 6
    a = "10"
    b = "99"
    
    a = reduce(a)
    print(countMagicNum(b)-countMagicNum(a))
    # print(countMagicNum(b))

    m = 2 
    d = 0
    a = "1"
    b = "9"
    
    a = reduce(a)
    print(countMagicNum(b)-countMagicNum(a))

    m = 19 
    d = 7
    a = "1000"
    b = "9999"
    
    a = reduce(a)
    print(countMagicNum(b)-countMagicNum(a))