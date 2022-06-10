# Given N, generate all strings of valid parenthesis
# N = 2
# (()), ()()


def generateValidParenthesis(n,output,i):

    if i == n*2:
        print(output)
        return 1

    ways = 0
    cnt_open = output.count("(")
    cnt_close = output.count(")")

    if cnt_open > cnt_close:
        output += ")"
        ways += generateValidParenthesis(n,output,i+1)
        output = output[:-1] # Backtracking
    if cnt_open < n:
        output += "("
        ways += generateValidParenthesis(n,output,i+1)
        output = output[:-1] # Backtracking

    return ways


if __name__=="__main__":
    
    for i in range(1,5):
        print("Generating Valid Parentheis for",i)
        print("Count of such ways is",generateValidParenthesis(i,"",0))
        
