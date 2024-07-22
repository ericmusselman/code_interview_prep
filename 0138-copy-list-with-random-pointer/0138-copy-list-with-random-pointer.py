"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        # old node is key, value is new node
        self.visited = {}
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head == None:
            return None
        
        if head in self.visited:
            return self.visited[head]
        
        node = Node(head.val, None, None)
        
        self.visited[head] = node # to deal with loops from random pointers
        
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        return node
    
    # O(n) in time and space