class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        path = []

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in path or word[i] != board[r][c]:
                return False
            path.append((r, c))
            res = dfs(r + 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c - 1, i + 1)
            path.remove((r, c))
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0): return True

        return False
    
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(Solution().exist(board, word))

board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word2 = "SEE"
print(Solution().exist(board2, word2))

board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word3 = "ABCB"
print(Solution().exist(board3, word3))