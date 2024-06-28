class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(i: int):
            num = 0
            for char in str(i):
                num += int(char)**2
            return num
        
        seen = set()
        while True:    
            n = next_num(n)
            
            if n == 1:
                return True
            
            if n not in seen:
                seen.add(n)
            else:
                return False
