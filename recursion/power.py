import sys


def power(b,e):
    if e == 0:
        return 1
    
    return b * power(b,e-1)

def fast_power(b,e):
    if e == 0:
        return 1
    half = fast_power(b,int(e/2))
    if e%2 == 0:
        return half * half
    else:
        return half * half * b

if __name__=="__main__":
    
    print(power(2,10))
    print(power(3,5))
    print(fast_power(2,10))
    print(fast_power(3,5))
    