import sys

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

if __name__=="__main__":
    fr = open("input.txt","r")
    fo = open("output.txt","w")
    sys.stdin = fr
    sys.stdout = fo
    n = int(input())
    
    print(fact(n))


    fr.close()
    fo.close()