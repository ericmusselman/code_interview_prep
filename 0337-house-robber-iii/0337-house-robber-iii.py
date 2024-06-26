# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            # return a two element list: [max if rob this node, max if not rob this node]
            if not node:
                return [0,0]
            left = helper(node.left)
            right = helper(node.right)
            
            # if we rob this node, we skip the children (so choose the second element)
            rob_value = node.val + left[1] + right[1]
            
            # if we do not rob this node, we choose for each child node
            not_rob_value = max(left) + max(right)
            
            return [rob_value, not_rob_value]
        
        return max(helper(root))
    
    # Time: O(n), Space: O(log(n) in worst case