# https://www.spoj.com/problems/PT07X/
# vertex Cover

from collections import deque
from queue import Empty


def dp(cur, take, par):

    if (cur,take) in memo:
        return memo[cur,take]
    ans = take

    # print(gr[cur])
    for ch in gr[cur]:
        if ch != par: # if ch is not the par node
            if take:
                ans += min(dp(ch,0,cur),dp(ch,1,cur))
            else:
                ans += dp(ch,1,cur)

    memo[cur,take] = ans
    return ans

def dfs(cur, par):
    
    dfs_dp[cur][0] = 0
    dfs_dp[cur][1] = 1
    for ch in gr[cur]:
        if ch != par:
            dfs(ch,cur)
            # After coming back from dfs, dp[x][*] will be filled
            dfs_dp[cur][0] += dfs_dp[ch][1]
            dfs_dp[cur][1] += min(dfs_dp[ch][1],dfs_dp[ch][0])

def bfs():
    q = deque()
    root = 0
    for i in range(n+1):
        if len(gr[i]) == 1:
            q.append(i)

    while len(q) != 0:
        cur = q.popleft()
        visited[cur] = 1
        root = cur

        bfs_dp[cur][0] = 0
        bfs_dp[cur][1] = 1

        for ch in gr[cur]:
            if visited[ch]:
                # child is the child
                bfs_dp[cur][0] += bfs_dp[ch][1]
                bfs_dp[cur][1] += min(bfs_dp[ch][0],bfs_dp[ch][1])
            else:
                # this is the parent (We are moving up)
                q.append(ch)

    # The node which is visited last is the root node
    return min(bfs_dp[root][0],bfs_dp[root][1])

if __name__ == "__main__":
    n = 3
    edges = [[1,2],[1,3]]
    gr = {}
    for i in range(n+1):
        gr[i] = []
    for e in edges:
        gr[e[0]].append(e[1])
        gr[e[1]].append(e[0])

    # DP Recursive Approach
    memo= {}
    print("DP Recursive Approach",min(dp(1,0,-1),dp(1,1,-1)))

    # DFS Approach
    dfs_dp = [[-1 for i in range(2)] for j in range(n+1)]
    dfs(1,0)
    print("DFS Approach",min(dfs_dp[1][0],dfs_dp[1][1]))

    # BFS Approach
    bfs_dp = [[-1 for i in range(2)] for j in range(n+1)]
    visited = [0 for i in range(n+1)]
    print("BFS Approach",bfs())



    n = 7
    edges = [[1,2],[1,3],[1,4],[2,5],[3,6],[4,7]]
    gr = {}
    for i in range(n+1):
        gr[i] = []
    for e in edges:
        gr[e[0]].append(e[1])
        gr[e[1]].append(e[0])

    # DP Recursive Approach
    memo= {}
    print("DP Recursive Approach",min(dp(1,0,-1),dp(1,1,-1)))

    # DFS Approach
    dfs_dp = [[-1 for i in range(2)] for j in range(n+1)]
    dfs(1,0)
    print("DFS Approach",min(dfs_dp[1][0],dfs_dp[1][1]))

    # BFS Approach
    bfs_dp = [[-1 for i in range(2)] for j in range(n+1)]
    visited = [0 for i in range(n+1)]
    print("BFS Approach",bfs())