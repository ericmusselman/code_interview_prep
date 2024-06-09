# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        queue = deque([root])
        output = []
        
        while queue:
            level_items = len(queue)
            curr_max = float("-inf")
            
            for _ in range(level_items):
                curr = queue.popleft()
                curr_max = max(curr_max, curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
            output.append(curr_max)
            
        return output
