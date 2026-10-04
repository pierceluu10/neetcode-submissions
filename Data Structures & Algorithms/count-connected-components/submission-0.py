from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set()
        comp = 0

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbour in adj_list[node]:
                dfs(neighbour)

        for node in range(n):
            if node not in visited:
                dfs(node)
                comp += 1
        return comp