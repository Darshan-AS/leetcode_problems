class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        n = len(letters)
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            l, r = (m + 1, r) if letters[m] <= target else (l, m - 1)
        return letters[l % n]
