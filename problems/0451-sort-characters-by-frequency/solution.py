class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        return ''.join(map(lambda x: x[0] * x[1], 
                       sorted(counter.items(), key=lambda x: x[1], reverse=True)))
