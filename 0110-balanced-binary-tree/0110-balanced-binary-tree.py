# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, root: Optional[TreeNode]) -> int:
            if not root:
                return -1
            else:
                left = self.depth(root.left)
                right = self.depth(root.right)
                return max(left, right) + 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return (
            abs(self.depth(root.left) - self.depth(root.right)) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        ) 
    
    # Time: O(n*log(n)), Space: O(n)
    