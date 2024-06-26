# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_distance = 0
        
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.search(root, start)
        return self.max_distance
    
    def search(self, root, start):
        depth = 0
        if root is None:
            return depth
        
        left = self.search(root.left, start)
        right = self.search(root.right, start)
        
        if root.val == start:
            self.max_distance = max(left, right)
            depth = -1
        elif left >= 0 and right >= 0:
            depth = max(left, right) + 1
        else:
            distance = abs(left) + abs(right)
            self.max_distance = max(self.max_distance, distance)
            depth = min(left, right) - 1
        return depth
        