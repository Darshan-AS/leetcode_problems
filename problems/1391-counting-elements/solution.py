class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr_set = set(arr)
        count = 0
        for i in arr:
            if i + 1 in arr_set:
                count += 1
        return count
