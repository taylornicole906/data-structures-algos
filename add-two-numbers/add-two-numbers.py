# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        carry = 0
        dummy = ListNode(0)
        current = dummy
        while l1 or l2:
            sum = carry
            if l1:
                sum += l1.val
            if l2:
                sum += l2.val
            if sum > 9:
                carry = sum // 10
                sum %= 10
            else:
                carry = 0
            current.next = ListNode(sum)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
          
        if carry > 0:
            current.next = ListNode(carry)
        return dummy.next  
        