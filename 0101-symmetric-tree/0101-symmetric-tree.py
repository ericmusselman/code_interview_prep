# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = [root, root]
        while queue:
            sub1 = queue.pop(0)
            sub2 = queue.pop(0)
            if sub1 is None and sub2 is None:
                continue
            if sub1 is None or sub2 is None:
                return False
            if sub1.val != sub2.val:
                return False
            queue.append(sub1.right)
            queue.append(sub2.left)
            queue.append(sub1.left)
            queue.append(sub2.right)
        return True
        # Time: O(n), Space: O(n)