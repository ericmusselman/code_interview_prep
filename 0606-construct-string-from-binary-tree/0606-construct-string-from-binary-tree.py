# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        output = []
        
        def dfs(root):
            # preorder
            if not root:
                return
            
            output.append("(")
            
            output.append(str(root.val))
            
            if not root.left and root.right:
                output.append("()")
            
            dfs(root.left)
            dfs(root.right)
            
            output.append(")")
            
        dfs(root)            
        return "".join(output)[1:-1]
        