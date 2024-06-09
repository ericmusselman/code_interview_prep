# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        self.search(root, output)
        return output
    
    def search(self, root, output):
        if not root:
            return
        else:
            self.search(root.left, output)
            output.append(root.val)
            self.search(root.right, output)
