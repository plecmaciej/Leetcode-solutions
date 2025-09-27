# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        value_map = {}
        if head == None:
            return False
        while head.next != None:
            if id(head) not in value_map:
                value_map[id(head)] = True
                head = head.next
            else:
                return True
            
        return False