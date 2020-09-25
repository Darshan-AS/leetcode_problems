class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        max_len = max(map(lambda x: len(x), nums_str))
        
        normalize = lambda n: (n + n[0] * (max_len - len(n)), n[-1])
        ans = ''.join(sorted(nums_str, key=normalize, reverse=True)).lstrip('0')
        return ans if ans else '0' 
