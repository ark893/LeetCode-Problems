# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        
        for i in range(n):
            fast = fast.next
            
        
        while fast and fast.next:                
            slow = slow.next
            fast = fast.next
            
        if fast is not None:
            slow.next = slow.next.next
        else:
            head = head.next
        
        return head