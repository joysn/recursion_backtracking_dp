# https://lightoj.com/problem/investigation
# An integer is divisible by 3 if the sum of its digits is also divisible by 3. 
# For example, 3702 is divisible by 3 and 12 (3+7+0+2) is also divisible by 3. This property also holds for the integer 9.

# In this problem, we will investigate this property for other integers.

# Input
# Input starts with an integer T (≤ 200), denoting the number of test cases.

# Each case contains three positive integers A, B and K (1 ≤ A ≤ B < 231 and 0 < K < 10000)>.

# Output
# For each case, output the case number and the number of integers in the range [A, B] which are divisible by K 
# and the sum of its digits is also divisible by K.

# Since we are taking mod at every step, 
# TIme complexity is 9 * 2 * k * k* = o(18k^2)
# 2^31 ~ 10^9, so at max 9 digits in a/b
debug = False
def countNumber(didx,last,sum_digit_mod,num_mod):
    global debug
    
    if didx == l:
        if sum_digit_mod == 0 and num_mod == 0:
            return 1
        else:
            return 0

    if (didx,last,sum_digit_mod,num_mod) in memo:
        return memo[didx,last,sum_digit_mod,num_mod]
    ans = 0
    if last:
        for i in range(int(solve.s[didx])+1):
            if i == int(solve.s[didx]):
                ans += countNumber(didx+1,True,(sum_digit_mod+i)%k,(num_mod*10+i)%k)
            else:
                ans += countNumber(didx+1,False,(sum_digit_mod+i)%k,(num_mod*10+i)%k)
    else:
        for i in range(10):
            ans += countNumber(didx+1,False,(sum_digit_mod+i)%k,(num_mod*10+i)%k)
    
    memo[didx,last,sum_digit_mod,num_mod] = ans
    return ans

def solve(s):
    global l
    global memo

    # Max sum can be only 90. So, if k > 90, then we will never have sum_digits_mod%k = 0
    if k > 90:
        return 0

    solve.s = s
    l = len(s)
    memo = {}
    return countNumber(0,True,0,0)

if __name__ == "__main__":
    s = ""
    a = 1
    b = 20
    k = 1
    print("Count",solve(str(b))-solve(str(a-1)))


    a = 1
    b = 20
    k = 2
    print("Count",solve(str(b))-solve(str(a-1)))


    a = 1
    b = 1000
    k = 4
    print("Count",solve(str(b))-solve(str(a-1)))
    