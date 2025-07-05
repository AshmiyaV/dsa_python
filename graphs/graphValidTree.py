class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if not n:
            return True

        grouped = {i: [] for i in range(n)}
        visited = set()

        for n1, n2 in edges:
            grouped[n1].append(n2)
            grouped[n2].append(n1)

        def dfs(i, prev):
            if i in visited:
                return False
            visited.add(i)
            for j in grouped[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
        
        return dfs(0, -1) and n == len(visited)