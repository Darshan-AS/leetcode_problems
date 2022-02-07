class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        buckets = [list() for _ in range(len(s) + 1)]
        
        for ch, count in counter.items():
            buckets[count].append(repeat(ch, count))
        
        flat_buckets = map(chain.from_iterable, reversed(buckets))
        return ''.join(chain.from_iterable(flat_buckets))
