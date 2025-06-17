from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        q = deque() #[count, time]

        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                val = 1 + heapq.heappop(maxHeap)
                if val:
                    q.append([val, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
    
tasks = ["A","A","A","B","B","B"]
n = 2
print(Solution().leastInterval(tasks, n))

tasks2 = ["A","C","A","B","D","B"]
n2 = 1
print(Solution().leastInterval(tasks2, n2))