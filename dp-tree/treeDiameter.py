# https://cses.fi/problemset/task/1131
# Tree Diameter


def dfs(cur, par):

    max_1, max_2 = 0,0
    for ch in gr[cur]:
        if ch != par:
            dfs(ch,cur)
            leafDist[cur] = max(leafDist[ch]+1, leafDist[cur])
            maxDia[cur] = max(maxDia[ch], maxDia[cur])
            
            if leafDist[ch] + 1 > max_1:
                max_2 = max_1
                max_1 = leafDist[ch] + 1
            elif leafDist[ch] + 1 > max_2:
                max_2 = leafDist[ch] + 1

    maxDia[cur] = max(maxDia[cur],max_1 + max_2)

if __name__ == "__main__":
    n = 7
    edges = [[1,2],[1,3],[1,4],[2,5],[3,6],[4,7]]
    gr = {}
    for i in range(n+1):
        gr[i] = []
    for e in edges:
        gr[e[0]].append(e[1])
        gr[e[1]].append(e[0])

    # DFS Approach
    leafDist = [0 for i in range(n+1)]
    maxDia = [0 for i in range(n+1)]
    dfs(1,0)
    print("DFS Approach",maxDia[1])

    n = 5
    edges = [[1,2],[1,3],[3,4],[3,5]]
    gr = {}
    for i in range(n+1):
        gr[i] = []
    for e in edges:
        gr[e[0]].append(e[1])
        gr[e[1]].append(e[0])

    # DFS Approach
    leafDist = [0 for i in range(n+1)]
    maxDia = [0 for i in range(n+1)]
    dfs(1,0)
    print("DFS Approach",maxDia[1])

