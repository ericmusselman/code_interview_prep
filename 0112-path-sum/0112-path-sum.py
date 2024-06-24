# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        targetSum -= root.val
        
        if not root.left and not root.right:  # at a leaf
            return targetSum == 0  # True if the sum is correct, False otherwise
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
    
    # Time: O(n), Space: O(log(n))
    