class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        dq = deque()
        for c in range(cols):
            if board[0][c] == "O":
                dq.append((0, c))
            if board[rows - 1][c] == "O":
                dq.append((rows - 1, c))
        
        for r in range(1, rows - 1):
            if board[r][0] == "O":
                dq.append((r, 0))
            if board[r][cols - 1] == "O":
                dq.append((r, cols - 1))


        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while dq:
            r, c = dq.pop()
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if 1 <= nr <= rows - 2 and 1 <= nc <= cols - 2 and board[nr][nc] == "O":
                    dq.append((nr, nc))
                    board[nr][nc] = "P"
        
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if board[r][c] == "P":
                    board[r][c] = "O"

            

            