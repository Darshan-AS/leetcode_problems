class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target_sum, remainder = divmod(sum(nums), k)
        if remainder:
            return False

        n = len(nums)

        def can_partition(
            remaining_buckets: int,
            current_bucket_sum: int,
            available_nums_at: AvailableNumsAt,
            start: int,
        ) -> bool:
            if not remaining_buckets:
                return not available_nums_at.has_available()

            if current_bucket_sum == target_sum:
                return can_partition(remaining_buckets - 1, 0, available_nums_at, 0)

            for i in range(start, n):
                num = nums[i]
                if (
                    available_nums_at.is_num_available_at(i)
                    and current_bucket_sum + num <= target_sum
                ):
                    if can_partition(
                        remaining_buckets,
                        current_bucket_sum + num,
                        available_nums_at.without_num_at(i),
                        i + 1,
                    ):
                        return True
            return False

        return can_partition(k, 0, AvailableNumsAt(n), 0)


class AvailableNumsAt:
    def __init__(self, n: int, mask: int =0) -> None:
        self.n = n
        self.mask = mask

    def without_num_at(self, index: int):
        mask = self.mask | (1 << index)
        return AvailableNumsAt(self.n, mask)

    def is_num_available_at(self, index: int) -> bool:
        return self.mask & (1 << index) == 0

    def has_available(self) -> bool:
        if self.mask == 0:
            return True
        # If all bits of a number are set, then adding 1 to it produces a number that is a perfect power of 2. AND-ing it with the number clears all bits of the number.
        return not ((self.mask + 1) & self.mask == 0)

