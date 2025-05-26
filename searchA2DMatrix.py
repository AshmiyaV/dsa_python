class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top = 0
        bot = ROWS - 1

        while top <= bot:
            m = (top + bot) // 2
            if target > matrix[m][-1]:
                top = m + 1
            elif target < matrix[m][0]:
                bot = m - 1
            else:
                break

        if not top <= bot:
            return False

        l = 0
        r = COLS - 1
        ROW = (top + bot) // 2
        while l <= r:
            m = (l + r) // 2
            if target > matrix[ROW][m]:
                l = m + 1
            elif target < matrix[ROW][m]:
                r = m - 1
            else:
                return True

        return False
    
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(Solution().searchMatrix(matrix, target))

matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target2 = 13
print(Solution().searchMatrix(matrix2, target2))