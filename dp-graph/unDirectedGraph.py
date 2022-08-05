# Graph to tree

def dfs(cur,par):
    global cycle
    visited.append(cur)
    print(cur)
    for ch in gr[cur]:
        if ch not in visited:
            dfs(ch,cur)
        elif ch != par:
            # backedge
            print("Backedge: ",cur,"->",ch)
            cycle = True
        

if __name__ == "__main__":

    n = 7
    edges = [[1,2],[1,3],[2,3],[2,4],[4,5],[5,6],[6,7],[7,4]]

    cycle = False
    gr = {}
    visited = []
    for i in range(n+1):
        gr[i] = []
    for e in edges:
        gr[e[0]].append(e[1])
        gr[e[1]].append(e[0])

    for i in range(1,n+1):
        if i not in visited:
            dfs(i,0)
    if cycle:
        print("Graph has a cycle")
