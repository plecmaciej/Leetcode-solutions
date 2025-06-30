# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        rest = 0
        sum_nums = 0
        anwser = l1
        while l1.next is not None and l2.next is not None:
            sum_nums = l1.val + l2.val + rest
            if sum_nums < 10:
                l1.val = sum_nums
                rest = 0
            else:
                l1.val = sum_nums % 10
                rest = 1

            l1 = l1.next
            l2 = l2.next
        

        if l2.next is None:
            sum_nums = l1.val + l2.val + rest
            if sum_nums < 10:
                l1.val = sum_nums
                return anwser
            else:
                l1.val = sum_nums % 10
                rest = 1
                while l1.next is not None:
                    l1 = l1.next
                    if l1.val + rest == 10:
                        l1.val = 0
                    else:
                        l1.val = l1.val + rest
                        return anwser
                if rest == 1:
                    l1.next = ListNode(rest)
        else:
            sum_nums = l1.val + l2.val + rest
            if sum_nums < 10:
                l1.val = sum_nums
                l1.next = l2.next
                return anwser
            else:
                l1.val = sum_nums % 10
                rest = 1
                l1.next = l2.next
                while l2.next is not None:
                    l2 = l2.next
                    if l2.val + rest == 10:
                        l2.val = 0
                    else:
                        l2.val = l2.val + rest
                        return anwser
                if rest == 1:
                    l2.next = ListNode(rest)
        return anwser

