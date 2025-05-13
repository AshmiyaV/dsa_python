from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)

        return list(res.values())
    
strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))

strs2 = [""]
print(Solution().groupAnagrams(strs2))

strs3 = ["a"]
print(Solution().groupAnagrams(strs3))