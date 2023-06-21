class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        n = len(nums)
        sort_order = itemgetter(*sorted(range(n), key=nums.__getitem__))
        
        s_nums = sort_order(nums)
        s_cost = sort_order(cost)
        prefix_cost = tuple(accumulate(s_cost))

        init_cost = sum(map(mul, s_nums, s_cost)) - s_nums[0] * prefix_cost[n - 1]
        get_next_cost = lambda a, i: a + (s_nums[i] - s_nums[i - 1]) * (2 * prefix_cost[i - 1] - prefix_cost[n - 1])
        return min(accumulate(range(1, n), get_next_cost, initial=init_cost))
