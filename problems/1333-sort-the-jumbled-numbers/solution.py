class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        def map_num(num: int) -> int:
            return int(''.join(map(lambda d: str(mapping[int(d)]), str(num))))
        
        return sorted(nums, key=map_num)
