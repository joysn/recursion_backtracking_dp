# Given N friends, going to a party, they can either go solo or pair up.
# FInd the total # of ways in which friends can be in the party 

def towerOfHanoi(n,fr,helper,to):
    if n == 0:
        return
    
    towerOfHanoi(n-1,fr,to,helper)
    print("Move ",fr,"->",to)
    towerOfHanoi(n-1,helper,fr,to)


if __name__=="__main__":
    
    for n in range(1,4):
        print("Move ",n," Discs")
        towerOfHanoi(n,'A','B','C')
    
