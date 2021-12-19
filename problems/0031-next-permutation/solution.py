class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def swap_inplace(i: int, j: int) -> None:
            nums[i], nums[j] = nums[j], nums[i]
        
        def reverse_inplace(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1
            
        
        n = len(nums)
        
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i < 0:
            reverse_inplace(0, n - 1)
            return
        
        j = n - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1

        swap_inplace(i, j)
        reverse_inplace(i + 1, n - 1)
        
