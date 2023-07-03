class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        match tuple(filter(lambda pair: ne(*pair), zip_longest(s, goal))):
            case (): return len(set(s)) != len(s)
            case ((a1, b1), (a2, b2)): return (a1, b1) == (b2, a2)
            case other: return False
