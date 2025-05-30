from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        
        elif list2:
            tail.next = list2

        return dummy.next

# Helper functions
def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)

# Test cases
list1 = build_linked_list([1, 2, 4])
list2 = build_linked_list([1, 3, 4])
result1 = Solution().mergeTwoLists(list1, list2)
print_linked_list(result1)

list3 = build_linked_list([])
list4 = build_linked_list([])
result2 = Solution().mergeTwoLists(list3, list4)
print_linked_list(result2)

list5 = build_linked_list([])
list6 = build_linked_list([0])
result3 = Solution().mergeTwoLists(list5, list6)
print_linked_list(result3)
