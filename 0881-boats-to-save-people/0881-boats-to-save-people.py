class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        # sort the people, start with the heaviest and try adding adding smallest
        smallest = 0
        biggest = len(people)-1
        people.sort()
        
        boats = 0
        
        while smallest <= biggest:
            boats += 1
            if people[smallest] + people[biggest] <= limit:
                smallest += 1
            biggest -= 1
        return boats
            
            
        