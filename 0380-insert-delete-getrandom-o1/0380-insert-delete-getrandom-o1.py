class RandomizedSet:

    def __init__(self):
        self.set = {} # val: index
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.set[val] = len(self.set)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.set:
            index = self.set[val]
            last_val = self.list[-1]
            self.list[index] = last_val
            self.set[last_val] = index
            
            self.list.pop()
            del self.set[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)
    
    # Notes: 
    # access last element of list in O(1), other indices would be O(n) ... append in O(1)
    # check/add/remove element from dict in O(1), access elements from dict in O(1)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()