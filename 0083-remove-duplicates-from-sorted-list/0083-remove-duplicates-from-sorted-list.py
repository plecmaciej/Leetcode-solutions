# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        temp = head
        if temp.next == None:
            return head
        if temp.next.next == None:

            if temp.val == temp.next.val:
                return temp.next
            else:
                return temp
        while temp.next.next != None:
            value = temp.val

            if temp.next.val == value:

                temp.next = temp.next.next
                
            else:
                temp = temp.next
            
        if temp.next.val == temp.val:
            temp.next = None
        return head
