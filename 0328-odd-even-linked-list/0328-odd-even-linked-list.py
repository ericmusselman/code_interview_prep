# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Sentinel nodes
        evens = ListNode(0)
        odds = ListNode(0)
        head_odd = odds
        head_even = evens
        isEven = False
        
        while head:
            
            # add head to even/odd, then advance head of even/odds
            if isEven:
                evens.next = head
                evens = evens.next
            else:
                odds.next = head
                odds = odds.next
                
            isEven = not isEven # alternate assignment based on index even/odd
            head = head.next # advance head of input
            
        evens.next = None
        odds.next = head_even.next # remove Sentinel
        
        return head_odd.next # remove Sentinel
    
    # Time: O(n)
    # Space: O(1)
        