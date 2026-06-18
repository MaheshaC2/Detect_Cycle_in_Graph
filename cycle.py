#Detect Cycle in Graph (DFS)

graph = {
    1: [2],
    2: [3],
    3: [1]
}
visited = set()
rec_stack = set()

def dfs(node):
    if node in rec_stack:
        return True
    if node in visited:
        return False

    visited.add(node)
    rec_stack.add(node)

    for neighbor in graph[node]:
        if dfs(neighbor):
            return True

    rec_stack.remove(node)
    return False

print(dfs(1))
