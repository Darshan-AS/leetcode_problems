class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        a, b = 0, 0
        prev_num = -math.inf
        for num, count in sorted(counter.items()):
            a, b = b, (max(a + num * count, b) if prev_num == num - 1 else b + num * count)
            prev_num = num
        return b
