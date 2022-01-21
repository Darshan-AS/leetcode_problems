class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Dutch national flag problem
        # [0, i) = 0, [i, j) = 1, [j, k] = unprocessed, (k, n] = 2
        i, j, k = 0, 0, len(nums) - 1
        
        while i <= j <= k:
            if nums[j] < 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] > 1:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1
            else:
                j += 1
        
            
        
