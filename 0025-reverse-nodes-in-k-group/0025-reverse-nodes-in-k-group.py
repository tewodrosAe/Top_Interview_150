# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        groupPrev = dummyNode
        
        while True:
            last = self.curGroup(groupPrev, k)
            if not last:
                break
            groupNext = last.next
            prev, current = last.next, groupPrev.next
            while current != groupNext:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            temp = groupPrev.next
            groupPrev.next = last
            groupPrev = temp
        return dummyNode.next
        
        
    def curGroup(self,current,k):
        while current and k > 0:
            current = current.next
            k -= 1
        return current