# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        seen = []
        
        current = head
        
        while current is not None:
            seen.append(current)
            current = current.next
            
            if current in seen:
                return current
             
            
        return
            
        