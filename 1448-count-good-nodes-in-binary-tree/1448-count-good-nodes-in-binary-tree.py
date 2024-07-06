# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
                
        def dfs(node, my_max):
            nonlocal answer
            if my_max <= node.val:
                answer += 1
            if node.left:
                dfs(node.left, max(node.val, my_max))
            if node.right:
                dfs(node.right, max(node.val, my_max))
        
        answer = 0
        max_seen = float('-inf')
        dfs(root, max_seen)
        return answer
        