class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        max_len = max(map(lambda x: len(str(x)), nums))
        
        def normalize(n):
            n_str = str(n)
            curr_len = len(n_str)
            return (n_str + n_str[0] * (max_len - curr_len), n_str[-1])
        
        ans = ''.join(map(str, sorted(nums, key=normalize, reverse=True))).lstrip('0')
        return ans if ans else '0' 
