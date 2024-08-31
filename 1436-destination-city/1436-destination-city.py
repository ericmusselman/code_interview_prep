class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing = set()
        for i in range(len(paths)):
            outgoing.add(paths[i][0])
        
        for i in range(len(paths)):
            test = paths[i][1]
            if test not in outgoing:
                return test
    
    # Time: O(n)
    # Space: O(n)