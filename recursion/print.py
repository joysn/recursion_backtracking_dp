import sys

def print_inc(n):
    if n == 0:
        return
    print_inc(n-1)
    print(n, end=" ")

def print_dec(n):
    if n == 0:
        return
    print(n,end=" ")
    print_dec(n-1)

if __name__=="__main__":
    
    print_inc(5)
    print("")
    print_dec(5)
    