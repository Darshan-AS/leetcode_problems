class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        return ''.join("0" if x[i] == "1" else "1" for i, x in enumerate(nums))
        
