class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        charMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(i, charStr):
            if i == len(digits):
                res.append(charStr)
                return
                        
            for c in charMap[digits[i]]:
                backtrack(i + 1, charStr + c)

        if digits:
            backtrack(0, "")

        return res