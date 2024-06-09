# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def dfs(node, lower, upper):
            # null node is valid tree
            if not node:
                return True
            
            # maintain binary tree property
            if not (lower < node.val < upper):
                return False
            
            left = dfs(node.left, lower, node.val)
            right = dfs(node.right, node.val, upper)
            
            return left and right
        
        return dfs(root, float("-inf"), float("inf"))        
        