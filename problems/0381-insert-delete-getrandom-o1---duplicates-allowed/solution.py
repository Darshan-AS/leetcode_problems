class RandomizedCollection:

    def __init__(self):
        self.value_to_index = defaultdict(set)
        self.values = []

    def insert(self, value: int) -> bool:
        self.values.append(value)
        self.value_to_index[value].add(len(self.values) - 1)
        
        return len(self.value_to_index[value]) == 1

    def remove(self, value: int) -> bool:
        if not self.value_to_index[value]: return False
        
        index = self.value_to_index[value].pop()
        last_value = self.values[-1]
        
        self.values[index], self.values[-1] = self.values[-1], self.values[index]
        self.values.pop()
        
        self.value_to_index[last_value].add(index)
        self.value_to_index[last_value].discard(len(self.values))
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
