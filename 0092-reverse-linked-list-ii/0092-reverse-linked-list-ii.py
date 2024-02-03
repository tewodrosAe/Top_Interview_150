# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp = ListNode(0, head)
        leftPrev, current = temp, head
        
        for i in range(left - 1):
            current, leftPrev = current.next, current
            
        
        prev = None
        
        for i in range(right-left+1):
            tempNode = current.next
            current.next = prev
            current, prev = tempNode,current
        leftPrev.next.next = current
        leftPrev.next = prev
        return temp.next
        
            