from itertools import accumulate


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        prefix_1_count = tuple(
            accumulate(s, lambda count, ch: count + (ch == "1"), initial=0)
        )
        suffix_0_count = tuple(
            reversed(
                tuple(
                    accumulate(
                        reversed(s),
                        lambda count, ch: count + (ch == "0"),
                        initial=0,
                    )
                )
            )
        )

        return min(map(lambda x: prefix_1_count[x] + suffix_0_count[x], range(len(s) + 1)))

