# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes_map = {}
        while headA != None:
            nodes_map[id(headA)] = headA
            headA = headA.next
        while headB != None:
            if id(headB) in nodes_map:
                return nodes_map[id(headB)]
            headB = headB.next
        return None