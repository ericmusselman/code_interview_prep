# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        # check for empty list
        if head is None:
            return False
        
        # can use a slow and fast pointer, and see if they are ever equal
        slow = head
        fast = head
        
        while fast and fast.next: # to avoid None at an end
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                return True
        
        return False