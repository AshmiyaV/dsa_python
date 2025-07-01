from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        visits = set()

        def addPath(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visits or grid[r][c] == -1:
                return
            visits.add((r, c))
            q.append((r, c))
        
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visits.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addPath(r + 1, c)
                addPath(r - 1, c)
                addPath(r, c + 1)
                addPath(r, c - 1)
            dist += 1