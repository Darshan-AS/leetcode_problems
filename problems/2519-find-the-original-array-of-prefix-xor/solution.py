class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        return list(starmap(xor, pairwise(chain((0,), pref))))
        
