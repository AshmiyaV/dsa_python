from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = { None: None }

        curr = head

        while curr:
            value = Node(curr.val)
            oldToNew[curr] = value
            curr = curr.next
        
        curr = head

        while curr:
            copy = oldToNew[curr]
            copy.next = oldToNew[curr.next]
            copy.random = oldToNew[curr.random]
            curr = curr.next
        
        return oldToNew[head]

def build_linked_list(data):
    if not data:
        return None
    nodes = [Node(val) for val, _ in data]
    for i, (_, rand_idx) in enumerate(data):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i+1]
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]
    return nodes[0]

def print_linked_list(head):
    res = []
    idx_map = {}
    idx = 0
    curr = head
    while curr:
        idx_map[curr] = idx
        curr = curr.next
        idx += 1

    curr = head
    while curr:
        random_idx = idx_map.get(curr.random, None)
        res.append([curr.val, random_idx])
        curr = curr.next
    print(res)

# Test cases
test_cases = [
    [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
    [[1, 1], [2, 1]],
    [[3, None], [3, 0], [3, None]]
]

solution = Solution()

for i, case in enumerate(test_cases, 1):
    print(f"Test case {i}:")
    head = build_linked_list(case)
    copied_head = solution.copyRandomList(head)
    print_linked_list(copied_head)
    print()
