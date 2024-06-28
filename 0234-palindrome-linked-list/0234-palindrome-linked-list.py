# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        sequence = []
        current = head
        while current is not None:
            sequence.append(current.val)
            current = current.next
        return sequence == sequence[::-1]
            
