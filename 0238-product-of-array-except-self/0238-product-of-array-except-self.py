class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        left_product, right_product, answer = [0]*n, [0]*n, [0]*n
        
        left_product[0], right_product[-1] = 1, 1
        for i in range(1, n):
            left_product[i] = left_product[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            right_product[i] = right_product[i+1] * nums[i+1]
            
        for i in range(n):
            answer[i] = left_product[i]*right_product[i]
        
        return answer
        