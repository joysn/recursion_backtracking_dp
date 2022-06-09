# Count # of Binarty Strings with no consecutive 1s that can be formed using length N
# 100, 101, 110, 1

def binaryStringCount(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    
    return binaryStringCount(n-2) + binaryStringCount(n-1)


if __name__=="__main__":
    
    for n in range(11):
        print(binaryStringCount(n), end = " ")
    
