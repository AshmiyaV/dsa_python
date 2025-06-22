from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


def print_examples():
    sol = Solution()
    examples = [
        {
            "candidates": [2, 3, 6, 7],
            "target": 7
        },
        {
            "candidates": [2, 3, 5],
            "target": 8
        },
        {
            "candidates": [2],
            "target": 1
        }
    ]

    for idx, ex in enumerate(examples, start=1):
        print(f"Example {idx}:")
        print(f"Input: candidates = {ex['candidates']}, target = {ex['target']}")
        output = sol.combinationSum(ex["candidates"], ex["target"])
        print(f"Output: {output}")
        print()


# Run the examples
print_examples()