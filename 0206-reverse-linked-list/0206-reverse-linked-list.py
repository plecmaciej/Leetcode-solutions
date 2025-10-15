# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        if head.next == None:
            return head
        prev_head = head
        head = head.next 
        prev_head.next = None
        while head.next != None:
            tmp_head2 = head
            head = head.next
            tmp_head2.next = prev_head
            prev_head = tmp_head2
        head.next = prev_head
        return head
