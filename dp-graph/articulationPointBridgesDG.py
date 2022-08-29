# Bridges and Articulaiton points for directed graph

def dfs(curr, par):

    global tme
    visited[curr] = 1
    tme += 1
    discovery[curr] = tme
    low_time[curr] = tme
    child_cnt = 0

    for ch in gr[curr]:
        if visited[ch] == 0:
            dfs(ch, curr)
            child_cnt += 1
            low_time[curr] = min(low_time[curr],low_time[ch])

            # bridges
            if low_time[ch] > discovery[curr]:
                bridges.add((curr,ch))

            # Articulation Point
            if low_time[ch] >= discovery[curr] and par != 0:
                articulation_points.add(curr)

        elif visited[ch] != 0 and ch != par:
            # Backedge
            low_time[curr] = min(low_time[curr],discovery[ch])

    if par == 0 and child_cnt > 1:
        articulation_points.add(curr)

if __name__ == "__main__":
    
    edges_list = [[[1,2],[3,1],[2,3],[2,4],[4,5],[5,6],[6,7],[7,4]]
                , [[1,2],[2,3],[3,4],[4,2],[3,5]]]
    for edges in edges_list:
        n = len(edges)

        gr = {}
        bridges = set()
        articulation_points = set()

        for i in range(n+1):
            gr[i] = []

        for e in edges:
            gr[e[0]].append(e[1])
            
        for i in range(1,n+1):
            visited = [0 for i in range(n+1)]
            discovery = [0 for i in range(n+1)]
            low_time = [0 for i in range(n+1)]
            tme = 0

            dfs(i,0)
        
        print("Edges",edges)
        print("Bridges",bridges)
        print("Articulation Points", articulation_points)

# Edges [[1, 2], [3, 1], [2, 3], [2, 4], [4, 5], [5, 6], [6, 7], [7, 4]]
# Bridges {(2, 4)}
# Articulation Points {2, 4}
# Edges [[1, 2], [2, 3], [3, 4], [4, 2], [3, 5]]
# Bridges {(1, 2), (3, 5)}
# Articulation Points {2, 3}
    