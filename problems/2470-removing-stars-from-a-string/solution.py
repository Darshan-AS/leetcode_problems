class Solution:
    def removeStars(self, s: str) -> str:
        return ''.join(reduce(lambda a, x: (a.pop() and a) if x == '*' else (a.append(x) or a), s, []))
