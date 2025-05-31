from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right= right.next

        left.next = left.next.next

        return dummy.next
    
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Test cases
solution = Solution()

print("Test 1: [1, 2, 3, 4], n = 2")
head1 = create_linked_list([1, 2, 3, 4])
result1 = solution.removeNthFromEnd(head1, 2)
print_linked_list(result1)

print("Test 2: [5], n = 1")
head2 = create_linked_list([5])
result2 = solution.removeNthFromEnd(head2, 1)
print_linked_list(result2)

print("Test 3: [1, 2], n = 2")
head3 = create_linked_list([1, 2])
result3 = solution.removeNthFromEnd(head3, 2)
print_linked_list(result3)
        