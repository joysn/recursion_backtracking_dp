# https://cses.fi/problemset/task/1133
# Tree Ditsance 2

def dfs_leaf_dist(cur, par):
    for ch in gr[cur]:
        if ch != par:
            dfs_leaf_dist(ch,cur)
            subtree_dist[cur] += subtree_dist[ch] + subtree_nodes[ch]*1
            subtree_nodes[cur] += subtree_nodes[ch]
    
def dfs_sum_distance(cur, par, sum_par):

    sum_dist[cur] = sum_par + (n-subtree_nodes[cur])
    for ch in gr[cur]:
        if ch != par:
            new_sum_par = sum_par + (n-subtree_nodes[cur])*1
            new_sum_par += subtree_dist[cur] - (subtree_dist[ch]+subtree_nodes[ch]*1)
            dfs_sum_distance(ch, cur, new_sum_par)
            sum_dist[cur] += subtree_dist[ch] + subtree_nodes[ch]*1

if __name__ == "__main__":
    n = 5
    edges = [[1,2],[1,3],[3,4],[3,5]]
    gr = {}
    for i in range(n+1):
        gr[i] = []
    for e in edges:
        gr[e[0]].append(e[1])
        gr[e[1]].append(e[0])

    subtree_dist = [0 for i in range(n+1)]
    subtree_nodes = [1 for i in range(n+1)]
    sum_dist = [0 for i in range(n+1)]
    dfs_leaf_dist(1,0)
    print("Sum Distance from leaves",subtree_dist)
    print("Nodes in subtree",subtree_nodes)
    dfs_sum_distance(1,0,0)
    print(sum_dist)