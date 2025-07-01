class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        atl, pac = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, ocean, height):
            if ((r, c) in ocean or  r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[r][c] < height):
                return
            ocean.add((r, c))
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])

        return res