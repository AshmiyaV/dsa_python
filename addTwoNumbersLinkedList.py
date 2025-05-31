from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            val = val1 + val2 + carry

            carry = val // 10
            val = val % 10

            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
    
def create_linked_list(lst):
    dummy = ListNode()
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Test cases
test_cases = [
    ([2, 4, 3], [5, 6, 4]),
    ([0], [0]),
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9])
]

solution = Solution()

for i, (l1_vals, l2_vals) in enumerate(test_cases, 1):
    l1 = create_linked_list(l1_vals)
    l2 = create_linked_list(l2_vals)
    result = solution.addTwoNumbers(l1, l2)
    print(f"Test case {i}:")
    print_linked_list(result)
    print()