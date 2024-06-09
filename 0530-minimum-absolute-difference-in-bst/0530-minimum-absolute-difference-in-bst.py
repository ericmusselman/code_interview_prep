# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node:
                return
            
            # INORDER DFS BINARY TREE results in sorted list
            left = dfs(node.left)
            values.append(node.val)
            right = dfs(node.right)
            
        values = []
        dfs(root)
        output = float("inf")
        
        for i in range(1, len(values)):
            output = min(output, values[i] - values[i-1]) # no need for abs here because of binary tree property
            
        return output
            