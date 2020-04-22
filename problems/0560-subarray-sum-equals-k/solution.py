class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_seen = defaultdict(int)
        
        sum_seen[0] = 1
        count = curr_sum = 0
        for i in nums:
            curr_sum += i
            count += sum_seen[curr_sum - k]
            sum_seen[curr_sum] += 1
        
        return count
