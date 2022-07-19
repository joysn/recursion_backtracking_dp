def dfs_leaf_dist(cur, par):
    # leaf nodes will not enter here
    for ch in gr[cur]:
        if ch!= par:
            dfs_leaf_dist(ch,cur)
            leaf_dist[cur] = max(leaf_dist[cur],leaf_dist[ch]+1)

def dfs_max_distance(cur, par, dist_par):

    max_1, max_2 = 0,0
    for ch in gr[cur]:
        if ch != par:
            if leaf_dist[ch] > max_1:
                max_2 = max_1
                max_1 = leaf_dist[ch]
            elif leaf_dist[ch] > max_2:
                max_2 = leaf_dist[ch]

    for ch in gr[cur]:
        if ch != par:
            new_dis_par = dist_par
            # for i in gr[cur]:
            #     if i != par and i!= ch:
            #         new_dis_par = max(new_dis_par,leaf_dist[i])

            if leaf_dist[ch] == max_1:
                new_dis_par = max(new_dis_par, max_2)
            else:
                new_dis_par = max(new_dis_par, max_1)

            dfs_max_distance(ch, cur,new_dis_par+1)
            max_dist[cur] = max(max_dist[cur], leaf_dist[ch]+1)

    max_dist[cur] = max(max_dist[cur], dist_par + 1)
    
if __name__ == "__main__":
    # n = 7
    # edges = [[1,2],[1,3],[1,4],[2,5],[3,6],[4,7]]
    # gr = {}
    # for i in range(n+1):
    #     gr[i] = []
    # for e in edges:
    #     gr[e[0]].append(e[1])
    #     gr[e[1]].append(e[0])

    # leaf_dist = [0 for i in range(n+1)]
    # max_dia = [0 for i in range(n+1)]
    # dfs(1,0)
    # print("Max Diameter by DFS", max_dia[1])

    n = 5
    edges = [[1,2],[1,3],[3,4],[3,5]]
    gr = {}
    for i in range(n+1):
        gr[i] = []
    for e in edges:
        gr[e[0]].append(e[1])
        gr[e[1]].append(e[0])

    leaf_dist = [0 for i in range(n+1)]
    max_dist = [0 for i in range(n+1)]
    dfs_leaf_dist(1,0)
    print("Max Distance from leaves",leaf_dist)
    dfs_max_distance(1,0,0)
    print("Max Distance from each node",max_dist)

