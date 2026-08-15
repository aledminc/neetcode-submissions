class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
        else:    
            hold = head.next 
            prev = head 
            head.next = None
            head = hold 
        while hold.next:
            hold = head.next 
            head.next = prev
            prev = head
            head = hold
        head.next = prev

        return head

