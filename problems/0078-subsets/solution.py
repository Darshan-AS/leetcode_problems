from itertools import compress

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def sub_sets(seq: list):
            yield from (
                compress(seq, map(int, reversed(bin(mask)[2:])))
                for mask in range(2 ** len(seq))
            )
        
        return list(sub_sets(nums))
