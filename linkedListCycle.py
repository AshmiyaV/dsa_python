from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False

def createLinkedList(values, pos):
    if not values:
        return None

    nodes = [ListNode(val) for val in values]
    for i in range(len(values) - 1):
        nodes[i].next = nodes[i + 1]
    
    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]

solution = Solution()

# Test Cases
head1 = createLinkedList([3,2,0,-4], 1)
head2 = createLinkedList([1,2], 0)
head3 = createLinkedList([1], -1)

print("Test 1:", solution.hasCycle(head1))  # True
print("Test 2:", solution.hasCycle(head2))  # True
print("Test 3:", solution.hasCycle(head3))  # False