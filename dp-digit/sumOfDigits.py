# https://www.spoj.com/problems/CPCRC1C/

def sumOfDigits(didx,last,sum,op):
    
    if didx == lb:
        # print(op,sum)
        return sum

    if (didx,last,sum) in memo:
        return memo[didx,last,sum]
    tsum = 0
    if last:
        for i in range(int(bstr[didx])+1):
            if i == int(bstr[didx]):
                tsum += sumOfDigits(didx+1,True,sum+i,op+str(i))
            else:    
                tsum += sumOfDigits(didx+1,False,sum+i,op+str(i))
    else: # middle
        for i in range(10):
            tsum += sumOfDigits(didx+1,False,sum+i,op+str(i))
    
    memo[didx,last,sum] = tsum
    return tsum


if __name__=="__main__":
    a = 1
    b = 10
    astr = str(a)
    la = len(astr)
    bstr = str(b)
    lb = len(bstr)
    if la < lb:
        astr = "0"*(lb-la)+astr
    sum = 0
    memo = {}
    for i in range(int(astr[0]),int(bstr[0])+1):
        if i == int(bstr[0]):
            sum += sumOfDigits(1,True,i,str(i))
        else:    
            sum += sumOfDigits(1,False,i,str(i))
        
    print("Sum is",sum)


    a = 100
    b = 777
    astr = str(a)
    la = len(astr)
    bstr = str(b)
    lb = len(bstr)
    if la < lb:
        astr = "0"*(lb-la)+astr
    sum = 0
    for i in range(int(astr[0]),int(bstr[0])+1):
        if i == int(bstr[0]):
            sum += sumOfDigits(1,True,i,str(i))
        else:    
            sum += sumOfDigits(1,False,i,str(i))
        
    print("Sum is",sum)