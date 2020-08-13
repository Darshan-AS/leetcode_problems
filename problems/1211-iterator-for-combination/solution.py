class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combination_gen = self.combination(characters, combinationLength)
        self.next_combination = next(self.combination_gen)

    def next(self) -> str:
        curr = self.next_combination
        try: self.next_combination = next(self.combination_gen)
        except StopIteration: self.next_combination = None
        return curr

    def hasNext(self) -> bool:
        return bool(self.next_combination)
        
    def combination(self, s, r):
        def helper(prefix, i):
            if len(prefix) == r:
                yield prefix
            for j in range(i, len(s)):
                yield from helper(prefix + s[j], j + 1)
        yield from helper('', 0)

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
