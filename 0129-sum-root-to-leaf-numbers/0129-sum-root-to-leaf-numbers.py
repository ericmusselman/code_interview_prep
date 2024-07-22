# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        stack = [(root, 0)]
        
        while stack:
            node, num = stack.pop()
            if node is not None:
                num = num*10 + node.val
            
                if node.left is None and node.right is None:
                    total += num
                else:
                    stack.append((node.left, num))
                    stack.append((node.right, num))
        
        return total
    
    # Time: O(n), Space: O(n) in worst case for the stack
        