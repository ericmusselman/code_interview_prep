class Solution:
    def candy(self, ratings: List[int]) -> int:
        total = 0
        n = len(ratings)
        left2right = [1] * n
        right2left = [1] * n
        
        # left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left2right[i] = left2right[i - 1] + 1
                
        # right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right2left[i] = right2left[i + 1] + 1
                
        # take the max
        for i in range(n):
            total += max(left2right[i], right2left[i])
        return total
    
    # Time O(n), Space O(n)
    # could also sort (and step, then sum at end) and get n*log(n) time
    