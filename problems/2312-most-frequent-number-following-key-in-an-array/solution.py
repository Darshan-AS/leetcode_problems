class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        return Counter(n for k, n in pairwise(nums) if k == key).most_common(1)[0][0]

