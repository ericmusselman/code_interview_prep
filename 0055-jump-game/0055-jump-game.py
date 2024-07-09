class Solution:
    def __init__(self):
        self.memo = []
        self.nums = []
    
    def canJumpFromPosition(self, position):
        
        # if unknown, look. otherwise, return the predetermined T/F
        if self.memo[position] != -1:
            return self.memo[position] == 1
        
        furthest = min(position + self.nums[position], len(self.nums)-1)
        for next_pos in range(position+1, furthest+1):
            if self.canJumpFromPosition(next_pos):
                self.memo[position] = 1
                return True
        
        self.memo[position] = 0
        return False
        
    def canJump(self, nums: List[int]) -> bool:
        self.nums = nums
        
        # initialize the memo
        # -1 for unknown, 0 for bad, 1 for good
        self.memo = [-1] * len(nums) 
        
        # add knowns to memo
        self.memo[-1] = 1 # last position is good
        
        return self.canJumpFromPosition(0)
        
    # Time: O(n^2), Space: O(n)
    