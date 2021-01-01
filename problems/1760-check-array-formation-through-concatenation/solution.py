class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pieces_map = {p[0]:p for p in pieces}
        return list(chain(*(pieces_map.get(i, []) for i in arr))) == arr
