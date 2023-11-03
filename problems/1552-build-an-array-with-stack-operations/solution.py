class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        return list(chain.from_iterable(
            islice(cycle(("Push", "Pop")), 2 * (b - a) - 1)
            for a, b in pairwise(chain((0,), target))
        ))
        
