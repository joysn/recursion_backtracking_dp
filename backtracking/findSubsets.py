# Give string, find all subsets
# abc = "",a,b,c,ab,ac,bc,abc


output =""
def findSubsets(input,output,i):
    # Base case
    if i >= len(input):
        if output == "":
            print("NULL")
        else:
            print(output)
        return
    # Recursive Case
    # Include the ith letter
    output += input[i]
    findSubsets(input,output,i+1)
    # Exclude the ith letter
    output = output[:-1]
    findSubsets(input,output,i+1)
    


if __name__=="__main__":
    

    findSubsets("abc","",0)
    
