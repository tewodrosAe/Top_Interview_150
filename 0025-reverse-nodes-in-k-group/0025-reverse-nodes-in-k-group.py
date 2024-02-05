# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        prevGroup = dummyNode
        
        while True:
            last = self.getLast(prevGroup,k)
            if not last:
                break
            prev, current = last.next, prevGroup.next
            lastNext = last.next
            while current != lastNext:
                temp = current.next
                current.next = prev
                prev = current
                current = temp 
            temp = prevGroup.next
            prevGroup.next = last
            prevGroup = temp
        return dummyNode.next
            
            
    def getLast(self,last,k):
        while k > 0 and last:
            last = last.next
            k -= 1
        return last