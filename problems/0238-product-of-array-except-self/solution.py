class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        products = [0] * length
        
        products[0] = 1
        for i in range(1, length):
            products[i] = products[i - 1] * nums[i - 1]
        
        r = 1
        for i in range(length - 1, -1, -1):
            products[i] = products[i] * r
            r *= nums[i]
        
        return products
