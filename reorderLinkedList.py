from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        prev = slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        first, second = head, prev
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

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
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "\n")
        curr = curr.next

solution = Solution()

print("Reordered list for [1, 2, 3, 4]:")
head1 = create_linked_list([1, 2, 3, 4])
solution.reorderList(head1)
print_linked_list(head1)

print("\nReordered list for [1, 2, 3, 4, 5]:")
head2 = create_linked_list([1, 2, 3, 4, 5])
solution.reorderList(head2)
print_linked_list(head2)