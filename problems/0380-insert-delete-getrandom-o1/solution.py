class RandomizedSet:

    def __init__(self):
        self.value_to_index = {}
        self.values = []

    def insert(self, value: int) -> bool:
        if value in self.value_to_index: return False
        
        self.values.append(value)
        self.value_to_index[value] = len(self.values) - 1
        
        return True

    def remove(self, value: int) -> bool:
        if value not in self.value_to_index: return False
        
        index = self.value_to_index[value]
        last_value = self.values[-1]
        
        self.values[index], self.values[-1] = self.values[-1], self.values[index]
        self.values.pop()
        
        self.value_to_index[last_value] = index
        del self.value_to_index[value]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
