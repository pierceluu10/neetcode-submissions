from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for neighbour in adj_list[node]:
                if neighbour == parent:
                    continue
                if neighbour in visited:
                    return False
                if not dfs(neighbour, node):
                    return False

            return True

        if not dfs(0, -1): #if there's a cycle
            return False
        if len(visited) != n: #if they're not all connected
            return False
        return True