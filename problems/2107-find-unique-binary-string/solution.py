class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        return ''.join(map({"0": "1", "1": "0"}.get, map(getitem, nums, count())))        
