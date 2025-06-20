from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()

            dfs(i + 1)

        dfs(0)
        return res

def print_examples():
    sol = Solution()
    examples = [
        {"nums": [1, 2, 3]},
        {"nums": [0]}
    ]

    for idx, example in enumerate(examples, start=1):
        print(f"Example {idx}:")
        print(f"Input: nums = {example['nums']}")
        output = sol.subsets(example["nums"])
        print("Output:", output)
        print()

print_examples()