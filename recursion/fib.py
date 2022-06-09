import sys

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__=="__main__":
    fr = open("input.txt","r")
    fo = open("output.txt","w")
    sys.stdin = fr
    sys.stdout = fo
    n = int(input())
    
    print(fib(n))


    fr.close()
    fo.close()