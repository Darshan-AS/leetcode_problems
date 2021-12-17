from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        for num in nums:
            if not lis or lis[-1] < num:
                lis.append(num)
            else:
                lis[bisect_left(lis, num)] = num
        
        return len(lis)
