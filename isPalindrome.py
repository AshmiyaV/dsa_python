class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isAlphaNumeric(s[l]):
                l += 1
            while r > l and not self.isAlphaNumeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1

        return True
        
    def isAlphaNumeric(self, c) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))
    
s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))

s2 = "race a car"
print(Solution().isPalindrome(s2))

s3 = " "
print(Solution().isPalindrome(s3))