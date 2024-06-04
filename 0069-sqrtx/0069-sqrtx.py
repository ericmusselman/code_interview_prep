class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<2:
            return x
        
        # try binary search O(logN)
        low, high = 0, x
        
        while (high-low) > 1:
            mp = (high+low)//2
            
            if mp*mp > x:
                high = mp
            else:
                low = mp
        return low
            