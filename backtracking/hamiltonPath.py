# Find all the hamilton paths
global visited
global adjacency_path

def dfs(curr,cnt,n):
    global path_exists
    if cnt == n:
        path_exists = True
        return

    visited[curr] = 1
    for x in adjacency_path[curr]:
        if visited[x] != 1:
            dfs(x,cnt+1,n)
            if path_exists:
                break
    visited[curr] = 0 # Backtracking
    return


if __name__=="__main__":

    nodes = 4
    adjacency_path = [
        [1],
        [0,2,3],
        [1,3],
        [2,1]
    ]
    
    visited = [0 for nodes in range(nodes)]
    for i in range(nodes):
        path_exists = False
        dfs(i,1,nodes)
        if not path_exists:
            print("Path does not exists starting from",i)
        else:
            print("Path exists starting from",i)
        
        
