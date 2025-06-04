from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeLists(l1, l2))

            lists = mergedLists
        
        return lists[0]

    def mergeLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next

        if l1:
            tail.next = l1

        elif l2:
            tail.next = l2
        
        return dummy.next
    
# Helpers to convert between list and linked list
def build_linked_list(values):
    dummy = ListNode()
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_result(input_lists):
    ll_inputs = [build_linked_list(lst) if lst else None for lst in input_lists]
    result = Solution().mergeKLists(ll_inputs)
    if result:
        print(result)
    else:
        print("None")

# --- Test cases ---
print("Input: [[1,4,5],[1,3,4],[2,6]]")
print_result([[1,4,5],[1,3,4],[2,6]])

print("\nInput: []")
print_result([])

print("\nInput: [[]]")
print_result([[]])