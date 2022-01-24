class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        suffix_max = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], suffix_max = suffix_max, max(suffix_max, arr[i])
        
        return arr
