from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.kthList(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next
    
    def kthList(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    
def build_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

# Helper to convert linked list to list
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Test cases
sol = Solution()

# Case 1
head1 = build_linked_list([1, 2, 3, 4, 5])
res1 = sol.reverseKGroup(head1, 2)
print_linked_list(res1)

# Case 2
head2 = build_linked_list([1, 2, 3, 4, 5])
res2 = sol.reverseKGroup(head2, 3)
print_linked_list(res2)