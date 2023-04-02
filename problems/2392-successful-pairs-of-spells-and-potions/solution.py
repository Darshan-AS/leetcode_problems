class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        f = partial(bisect.bisect_left, sorted(potions))
        return (len(potions) - f(success / x) for x in spells)
