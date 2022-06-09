# Given N friends, going to a party, they can either go solo or pair up.
# FInd the total # of ways in which friends can be in the party 

def partyCount(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    return (n-1)*partyCount(n-2) + partyCount(n-1)


if __name__=="__main__":
    
    for n in range(11):
        print(partyCount(n), end = " ")
    
