# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = head
        fast = head
        output = 0

        # get to middle with slow
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        curr = slow
        prev = None
            
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # sum it up
        start = head
        while prev:
            output = max(output, start.val+prev.val)
            prev = prev.next
            start = start.next

        return output
    
    # Time: O(n), Space: O(1)
        