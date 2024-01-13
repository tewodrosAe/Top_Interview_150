# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = False
        output = ListNode()
        current = output
        while l1 or l2:
            num = (l1.val if l1 else 0) + (l2.val if l2 else 0)
            if prev:
                num += 1
                prev = False
            if num > 9:
                num = num % 10
                prev = True
            current.next = ListNode(num)
            current = current.next
            l1= l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if prev:
            current.next = ListNode(1)
        return output.next