# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # find node in the middle
        
        # 1xy 2 3 4 5
        # 1 2x 3y 4 5
        # 1 2 3x 4 5y STOP HERE
        
        # 1xy 2 3 4 5 6
        # 1 2x 3y 4 5 6
        # 1 2 3x 4 5y 6 STOP HERE
        # 1 2 3 4x 5 6 _y
        # if the 2 stepper runs out of elements then its even
        
        # Deal with one node case:
        if head.next == None:
            return None
        
        slow = head
        fast = head.next.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # ^ fast just reached the end, so skip the next node
        slow.next = slow.next.next
        
        return head
        
    # Time: O(n)
    # Space: O(1)
    