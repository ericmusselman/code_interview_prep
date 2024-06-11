class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        
        roads = set()
        graph = defaultdict(list)
        seen = {0}
        
        for ai, bi in connections:
            graph[ai].append(bi)
            graph[bi].append(ai)
            roads.add((ai, bi))
        
        def dfs(node):
            output = 0
            for neighbor in graph[node]:
                if neighbor not in seen:
                    if (node, neighbor) in roads:
                        output += 1
                    seen.add(neighbor)
                    output += dfs(neighbor)
            return output
                    
        return dfs(0)
    