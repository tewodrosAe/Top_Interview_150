class RandomizedSet:

    def __init__(self):
        self.colMap = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        exist = val not in self.colMap
        if exist:
            self.colMap[val] = len(self.arr)
            self.arr.append(val)
        return exist

    def remove(self, val: int) -> bool:
        exist = val in self.colMap
        if exist:
            index = self.colMap[val]
            last = self.arr[-1]
            self.arr[index] = last
            self.arr.pop()
            self.colMap[last] = index
            del self.colMap[val]
        return exist 

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()