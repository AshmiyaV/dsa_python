class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeObjects = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in closeObjects:
                if stack and stack[-1] == closeObjects[c]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(c)

        return True if not stack else False
    
s = "()"
print(Solution().isValid(s))

s2 = "()[]{}"
print(Solution().isValid(s2))

s3 = "(]"
print(Solution().isValid(s3))

s4 = "([])"
print(Solution().isValid(s4))