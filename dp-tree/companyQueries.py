# https://cses.fi/problemset/task/1687
# Company Queries I

def findBoss(e,level):
    if level == 0:
        return e
    if e >= 0:
        return findBoss(bosses[e],level-1)
    return -1

# Fill up the parents
def dfs(cur, par):
    ancestors[cur][0] = par
    for l in range(1,maxLevel):
        ancestors[cur][l] = ancestors[ancestors[cur][l-1]][l-1]
    for ch in gr[cur]:
        if ch!= par:
            dfs(ch,cur)


def giveLthParent(node, level):
    cur = node
    for l in range(maxLevel):
        if ((level>>l) & 1):
            cur = ancestors[cur][l]
    if cur == 0:
        cur = -1
    return cur

if __name__ == "__main__":

    maxLevel = 20

    n, q = 5, 3
    bosses = [-1,-1,1, 1, 3, 3]
    queries = [[4, 1],[4, 2],[4, 3]]

    print(findBoss(4,1))
    print(findBoss(4,2))
    print(findBoss(4,3))

    gr = {}
    ancestors = {}
    for i in range(n+1):
        gr[i] = []
        ancestors[i] = [0]*maxLevel

    for i in range(2,n+1):
        gr[i].append(bosses[i])
        gr[bosses[i]].append(i)
    print(gr)
    # print(ancestors)

    dfs(1,0)
    # Check the parents
    # for node in range(1,n+1):
    #     for l in range(3):
    #         print(node, pow(2,l),ancestors[node][l])

    for q in queries:
        node = q[0]
        level = q[1]
        print(giveLthParent(node, level))
