class MyHashMap:

    def __init__(self):
        self.M = 1000
        self.hm = [list() for _ in range(self.M)]

    def put(self, key: int, value: int) -> None:
        chain = self.hm[key % self.M]
        i = self.__index_chain(chain, key)
        
        if i == -1: chain.append([key, value])
        else: chain[i][1] = value

    def get(self, key: int) -> int:
        chain = self.hm[key % self.M]
        i = self.__index_chain(chain, key)
        
        if i == -1: return -1
        else: return chain[i][1]

    def remove(self, key: int) -> None:
        chain = self.hm[key % self.M]
        i = self.__index_chain(chain, key)
        
        if i == -1: return
        else: chain.pop(i)
    
    def __index_chain(self, chain: list, key: int, default: int = -1) -> int:
        for i, (k, _) in enumerate(chain):
            if k == key: return i
        return default


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
