# Articulation Point and Bridges in Undirected Graph

from turtle import distance


def dfs(curr,par):

    global tme

    visited[curr] = 1
    tme += 1
    discovery[curr] = tme
    low_time[curr] = tme
    child_cnt = 0

    for ch in gr[curr]:
        if visited[ch] == 0:
            dfs(ch,curr)
            child_cnt += 1
            low_time[curr] = min(low_time[curr],low_time[ch])

            # Bridges
            if low_time[ch] > discovery[curr]:
                bridges.append((curr,ch))

            # Articulation Point for non root node
            if par != 0 and low_time[ch] >= discovery[curr]:
                articulation_point.add(curr)

        elif visited[ch] != 0 and ch != par:
            # Backedge
            low_time[curr] = min(low_time[curr],discovery[ch])

    if par == 0 and child_cnt > 1:
        articulation_point.append(curr)

        
    

if __name__ == "__main__":

    n = 7
    edges = [[1,2],[1,3],[2,3],[2,4],[4,5],[5,6],[6,7],[4,7]]

    gr = {}
    for i in range(n+1):
        gr[i] = []
    
    for e in edges:
        gr[e[0]].append(e[1])
        gr[e[1]].append(e[0])

    visited = [0 for i in range(n+1)]
    discovery = [0 for i in range(n+1)]
    low_time = [0 for i in range(n+1)]
    tme = 0

    bridges = []
    articulation_point = set()
        
    dfs(1,0)

    print(articulation_point)
    print(bridges)