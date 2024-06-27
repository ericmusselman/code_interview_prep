"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return root
        
        # BFS - deque, end each level with a null
        queue = deque([root])
        
        while queue:
            n = len(queue)
            
            for i in range(n):
                node = queue.popleft()
                
                # so the last element's next remains None
                if i < n - 1:
                    node.next = queue[0]
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)  
        
        return root
    