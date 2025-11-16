# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        prev = ListNode()
        prev = head
        cur = head.next

        while cur != None:
            print(prev.val)
            print(cur.val)
            if cur.val == prev.val:
                prev.next = cur.next
            else:    
                prev = prev.next
            
            cur = cur.next
            
        return head