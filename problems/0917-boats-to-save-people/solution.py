class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        ps = sorted(people)
        boats = 0

        i, j = 0, len(ps) - 1
        while i <= j:
            i = i + 1 if ps[i] + ps[j] <= limit else i
            j -= 1
            boats += 1
        return boats
