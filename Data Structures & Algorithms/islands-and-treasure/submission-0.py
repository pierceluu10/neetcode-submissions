class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        dq = deque()

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    dq.append((r, c))
                    


        while dq:
            cr, cc = dq.popleft()
            dist = grid[cr][cc]
            for d in dirs:
                nr, nc = cr + d[0], cc + d[1]
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                    if dist + 1 < grid[nr][nc]:
                        grid[nr][nc] = dist + 1
                        dq.append((nr, nc))