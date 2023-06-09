class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        return letters[bisect_right(letters, target) % len(letters)]
