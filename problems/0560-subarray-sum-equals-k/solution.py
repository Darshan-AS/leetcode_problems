class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_seen = defaultdict(int, {0: 1}) # {sum: no of times ecountered}
        
        curr_sum = count = 0
        for num in nums:
            curr_sum += num
            count += sum_seen[curr_sum - k]
            sum_seen[curr_sum] += 1
        
        return count
