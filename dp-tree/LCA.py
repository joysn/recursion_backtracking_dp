# https://cses.fi/problemset/task/1688
# LCA

def dfs(cur, par):
    ancestors[cur][0] = par
    depth[cur] = depth[par]+1
    for i in range(1,maxLevel):
        ancestors[cur][i] = ancestors[ancestors[cur][i-1]][i-1]
    for ch in gr[cur]:
        if ch != par:
            dfs(ch,cur)


def getLthParent(node,level):
    cur = node
    for l in range(maxLevel):
        # lth bit of level is set
        if (level>>l)&1:
            cur = ancestors[cur][l]
    return cur
    

def getLCA(u,v):
    if u == v:
        return u

    if depth[u] < depth[v]:
        u,v = v,u

    diff = depth[u] - depth[v]
    if diff != 0:
        u = getLthParent(u,diff)
    
    if u == v:
        return u
    for l in range(maxLevel-1,-1,-1):
        if ancestors[u][l] != ancestors[v][l]:
            u = ancestors[u][l]
            v = ancestors[v][l]
    return ancestors[u][0]


# def getDistanceBetween(u,v):
#     if u == v:
#         return 0
#     lca = getLCA(u,v)
#     return (depth[u]-depth[lca]) + (depth[v]-depth[lca])

if __name__ == "__main__":

    maxLevel = 20

    n = 5 
    q = 3
    tree = [1, 1, 3, 3]
    queries = [[4,5],[2,5],[1,4]]

    gr = {}
    ancestors = {}
    depth = {}
    for i in range(n+1):
        depth[i] = 0
        gr[i] = []
        ancestors[i] = [0]*maxLevel
    for i in range(2,n+1):
        gr[i].append(tree[i-2])
        gr[tree[i-2]].append(i)

    dfs(1,0)

    # # Check the parents
    # for node in range(1,n+1):
    #     for l in range(3):
    #         print(node, pow(2,l),ancestors[node][l])

    for q in queries:
        print("LCA of",q," is ",getLCA(q[0],q[1]))
        # print("Length between",q," is",getDistanceBetween(q[0],q[1]))

