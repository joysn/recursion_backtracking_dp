

def get_autobiographical_number(idx):
    global n
    global count
    global number

    # Base case
    if idx == n:
        # Check
        for i in range(n):
            if count[i] != number[i]:
                return
        str_num = [str(i) for i in number]
        print("".join(str_num))
        return
    
    for i in range(n):

        number[idx] = i
        count[i] += 1

        get_autobiographical_number(idx+1)

        count[i] -= 1
        number[idx] = -1



if __name__ == "__main__":
    
    n = 4
    count = [0 for i in range(n)]
    number = [-1 for i in range(n)]
    get_autobiographical_number(0)