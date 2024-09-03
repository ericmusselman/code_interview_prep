# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr_val = root.val
        p_val = p.val
        q_val = q.val
        
        if p_val > curr_val and q_val > curr_val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < curr_val and q_val < curr_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            # one left, one right AKA LCA
            return root
        
    # Time: O(N)
    # Space: O(N)