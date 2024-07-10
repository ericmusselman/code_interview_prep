class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, curr = 0, 0
        answer = 0
        
        for i in range(len(gas)):
            total += gas[i] - cost[i] # if this doesnt finish >= 0 then it is impossible
            curr += gas[i] - cost[i]
            
            # if we find a valley
            if curr < 0:
                curr = 0
                answer = i+1
        
        return answer if total >= 0 else -1
        
        # Time: O(n), Space: O(1)