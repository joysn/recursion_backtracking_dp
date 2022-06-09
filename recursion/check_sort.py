import sys

def ifSorted(arr):

    if len(arr) < 2:
        return True
    
    if (arr[0] < arr[1]) and ifSorted(arr[1:]):
        return True
    
    return False

if __name__=="__main__":
    
    print(ifSorted([1,2,5,3,6,4]))
    print(ifSorted([1,2,3,4,5,6]))