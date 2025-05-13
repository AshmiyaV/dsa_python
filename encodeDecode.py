class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
    
strs = ["neet","code","love","you"]
encoded = Solution().encode(strs)
print(encoded)
print(Solution().decode(encoded))

strs2 = ["we","say",":","yes"]
encoded2 = Solution().encode(strs2)
print(encoded2)
print(Solution().decode(encoded2))

 