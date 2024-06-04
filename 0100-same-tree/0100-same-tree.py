# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        #  O(n) with recursion
        if not p and not q: # both None, no need to look deeper
            return True
        
        if not p or not q: # as in, both not None
            return False

        if p.val != q.val: # obvious, can check for val finally bc we know not NoneType
            return False
        
        # we have to look deeper, matching at this node
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        