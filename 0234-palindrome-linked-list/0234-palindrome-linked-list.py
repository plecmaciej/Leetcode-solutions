# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # Znajdź środek listy (powolny wskaźnik 'slow' będzie na środku)
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Odwróć drugą połowę listy
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # Porównaj pierwszą i drugą połowę listy
        left, right = head, prev
        while right:  # Porównujemy tylko drugą połowę
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True