class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        get = lambda xs, i: xs[i] if i < n else inf # To avoid using nums.append(inf)

        @cache
        def lis_len_count(i: int) -> tuple[int, int]: # Index -> (LIS length, LIS count) ending at Index
            len_counts = [lis_len_count(j) for j in range(min(i, n)) if get(nums, j) < get(nums, i)]
            m_len = max(len_counts, default=(0, 0))[0]
            return m_len + 1, max(sum(c for l, c in len_counts if l == m_len), 1)
        
        return lis_len_count(n)[1]
