class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = count = 0
        while count < n:
            j, temp = (i + k) % n, nums[i]
            while count < n:
                nums[j], temp = temp, nums[j]
                count += 1
                if j == i:
                    break
                else:
                    j = (j + k) % n
            i += 1

