# Given N friends, going to a party, they can either go solo or pair up.
# FInd the total # of ways in which friends can be in the party 

def partyCount(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    return (n-1)*partyCount(n-2) + partyCount(n-1)


def partyCountTab():
    
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    if n >= 1:
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = (i-1)*dp[i-2] + dp[i-1]

    return dp[-1]

if __name__=="__main__":
    
    print("Top Down",)
    for n in range(11):
        print(partyCount(n), end = " ")
    print()
    print("Bottom Up")
    for n in range(11):
        print(partyCountTab(), end = " ")
    
