# Print all number from 0 to the givin number

def printNumbers(didx,last,op):
    
    if didx >= l:
        print("".join(op))
        return
    
    if not last:
        for i in range(10):
            printNumbers(didx+1,False,op+[str(i)])
    else:
        for i in range(int(nstr[didx])+1):
            if i == int(nstr[didx]):
                printNumbers(didx+1,True,op+[str(i)])
            else:
                printNumbers(didx+1,False,op+[str(i)])
        


if __name__=="__main__":
    n = 2
    nstr = str(n)
    l = len(nstr)
    printNumbers(0,True,[])