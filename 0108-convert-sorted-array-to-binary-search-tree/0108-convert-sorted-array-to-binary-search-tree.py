# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # pre-rder, choose left middle
        def branch(left, right):
            if left > right:
                return None
            
            index = (left+right)//2  # left middle, from floor division
            root = TreeNode(nums[index])
            root.left = branch(left, index-1)
            root.right = branch(index+1, right)
            return root
        
        return branch(0, len(nums)-1)
        
        # Time: O(n), Space: O(log(n))
            