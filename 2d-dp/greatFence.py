# https://codeforces.com/problemset/problem/1221/D
# D. Make The Fence Great Again

# You have a fence consisting of n vertical boards. The width of each board is 1. The height of the i-th board is ai. 
# You think that the fence is great if there is no pair of adjacent boards having the same height. More formally, 
# the fence is great if and only if for all indices from 2 to n, the condition ai−1≠ai holds.

# Unfortunately, it is possible that now your fence is not great. But you can change it! You can increase the length of 
# the i-th board by 1, but you have to pay bi rubles for it. The length of each board can be increased any number of 
# times (possibly, zero).
# Calculate the minimum number of rubles you have to spend to make the fence great again!

# n = 3
# heights = [2,2,3]
# cost = [4,1,5]
# Output = 2

# n = 3
# heights = [2,2,2]
# cost= [3,10,6]
# Output = 9

# n = 4
# heights = [1,3,2,1000000000]
# cost = [7,3,6,2]
# Output = 0
import sys

def costGreatFence(idx,prev_height):
    if idx == n:
        return 0

    min_cost = sys.maxsize
    if heights[idx] == prev_height:
        # Need to make change
        min_cost = min(min_cost,cost[idx]+costGreatFence(idx+1,heights[idx]+1), cost[idx-1]+costGreatFence(idx+1,heights[idx]))
    else:
        min_cost = min(min_cost, costGreatFence(idx+1,heights[idx]))

    # print(idx, min_cost)
    return min_cost
    
def costGreatFenceTab():
    dp = [[-1 for i in range(n)] for j in range(3)]

    min_cost = sys.maxsize
    for c in range(n):
        for r in range(3):
            if c == 0:
                dp[r][c] = cost[c]*r
            else:
                dp[r][c] = min(dp[x][c-1]+cost[c]*r for x in range(3) if heights[c-1]+x!=heights[c]+r)
            if c == n-1 and min_cost > dp[r][c]:
                min_cost = dp[r][c]
    # for e in dp:
    #     print(e)
    return min_cost

if __name__=="__main__":

    n = 3
    heights = [2,2,3]
    cost = [4,1,5]
    # Output = 2
    print("Top Down",costGreatFence(0,0))
    print("Bottum Up",costGreatFenceTab())

    n = 3
    heights = [2,2,2]
    cost= [3,10,6]
    print("Top Down",costGreatFence(0,0))
    print("Bottum Up",costGreatFenceTab())
    # Output = 9

    n = 4
    heights = [1,3,2,1000000000]
    cost = [7,3,6,2]
    print("Top Down",costGreatFence(0,0))
    print("Bottum Up",costGreatFenceTab())
    # Output = 0