class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        indegree = [0]*n
        for x, y in edges:
            indegree[y] += 1
        
        output = []
        for node in range(n):
            if indegree[node] == 0:
                output.append(node)
        return output
    