import sys


def tiling_ways(n):
    if n < 4:
        return 1
    
    return tiling_ways(n-1) + tiling_ways(n-4)


if __name__=="__main__":
    
    for n in range(1,11):
        print(tiling_ways(n), end = " ")
    
