class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
                    
        combos = len(isConnected)
        graph = defaultdict(list)
        for i in range(combos):
            for j in range(i+1, combos): # don't need to check with itself, and only upper-right triangle
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        seen = set()
        output = 0
        
        for i in range(combos):
            if i not in seen:
                output += 1
                seen.add(i)
                dfs(i)
                
        return output