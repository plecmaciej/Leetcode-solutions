# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]: 
        while head and head.val == val:
            head = head.next
        if head == None:
            return None
        tmp_head = head 
        while tmp_head.next != None:
            if tmp_head.next.val == val:
                tmp_head.next = tmp_head.next.next
            else:
                tmp_head = tmp_head.next
        return head
