class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        # greedy: choose the affordable project with the most profits
        # heap to keep track of most profitable project we can afford
        
        projects = sorted(zip(capital, profits))
        n_projects = len(projects)
        i = 0
        
        # 1) find profits we can afford and put them on the max heap
        profits_heap = []
        for _ in range(k): # only allowed k total projects
            # consider projects we can afford
            while i < n_projects and projects[i][0] <= w: 
                heapq.heappush(profits_heap, -projects[i][1])
                i+=1
                
            if len(profits_heap) == 0:
                return w

            # 2) of the affordable projects, which is the most profitable
            w += abs(heapq.heappop(profits_heap))
        
        return w
        