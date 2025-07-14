# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        output = head 
        while head.next != None:
            head.val, head.next.val = head.next.val, head.val
            if head.next.next != None:
                head = head.next.next
            else:
                break
        return output
