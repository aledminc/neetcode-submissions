# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 and not list2:
            return list1
        if list2 and not list1:
            return list2
        if not list2 and not list1:
            return list1

        out = []

        if list1.val > list2.val:
            out.append(list2)
            list2 = list2.next
        else:
            out.append(list1)
            list1 = list1.next
        
        while list1 and list2:
            print(list1.val, list2.val)
            if list1.val > list2.val:
                out[-1].next = list2
                out.append(list2)
                list2 = list2.next
            else:
                out[-1].next = list1
                out.append(list1)
                list1 = list1.next

        if list1:
            out[-1].next = list1
        elif list2:
            out[-1].next = list2

        return out[0]

