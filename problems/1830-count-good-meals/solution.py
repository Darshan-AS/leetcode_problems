class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        def two_sum_count(counter: dict[int, int], target: int) -> int:
            return sum(
                (((counter[y] * counter[x]) / 2) if x != y else ((counter[x] - 1) * counter[x]) / 2)
                for x in counter
                for y in (target - x,)
            )
            
        def powers_of_2() -> Iterator[int]:
            n = 1
            while True:
                yield n
                n <<= 1
        
        deliciousness_counter = Counter(deliciousness)
        max_deliciousness = max(deliciousness_counter)
        le_max_deliciousness = lambda x: x <= 2 * max_deliciousness
        M = 1_000_000_007
        
        return int(sum(
            two_sum_count(deliciousness_counter, p) % M
            for p in takewhile(le_max_deliciousness, powers_of_2())
        )) % M
                
