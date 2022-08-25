
def dfs(cur , par):
    global cycle
    # Visisted and in call stack
    visited[cur] = 1
    for ch in gr[cur]:
        if visited[ch] == 0:
            dfs(ch,cur)   
        elif ch != par and visited[ch] == 1:
            print("Backedge: ",cur,"->",ch)
            cycle = True 
    # Visisted and not in call stack
    visited[cur] = 2

if __name__ == "__main__":

    n = 7
    edges = [[1,2],[1,3],[2,3],[2,4],[4,5],[5,6],[6,7],[7,4]]

    cycle = False
    gr = {}
    visited = []
    for i in range(n+1):
        gr[i] = []
        visited.append(i)
        visited[i] = 0
    for e in edges:
        gr[e[0]].append(e[1])
        # gr[e[1]].append(e[0])

    for i in range(1,n+1):
        if visited[i] == 0:
            dfs(i,0)
    if cycle:
        print("Graph has a cycle")
