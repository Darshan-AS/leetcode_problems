class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        return sum(map(mod, Counter(chain.from_iterable(words)).values(), repeat(len(words)))) == 0
        
