# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None:
            return list2
        if list2 == None:
            return list1
        list3 = ListNode()
        head = list3
        if list1.val < list2.val:
            list3 = list1
            head = list3
            if list1.next is None:
                list3.next = list2
                return head
            list1 = list1.next
        else:
            list3 = list2
            head = list3
            if list2.next is None:
                list3.next = list1
                return head
            list2 = list2.next
        while list1.next is not None :
            if list2.next is None:
                if list1.val < list2.val:
                    list3.next = list1
                    list1 = list1.next
                    list3 = list3.next
                else:
                    list3.next = list2
                    list3 = list3.next
                    list3.next = list1
                    return head
            elif list1.val < list2.val:
                list3.next = list1
                list1 = list1.next
                list3 = list3.next
            else:
                list3.next = list2
                list2 = list2.next
                list3 = list3.next

        while list2.next is not None :
            
            if list1.val < list2.val:
                list3.next = list1
                list3 = list3.next
                list3.next = list2
                return head
            else:
                list3.next = list2
                list3 = list3.next
                list2 = list2.next
        
        if list1.val < list2.val:
            list3.next = list1
            list3 = list3.next
            list3.next = list2
        else:
            list3.next = list2
            list3 = list3.next
            list3.next = list1

        return head