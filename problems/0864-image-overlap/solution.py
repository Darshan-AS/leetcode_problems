class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        A = [(i, j) for i, row in enumerate(img1) for j, item in enumerate(row) if item]
        B = [(i, j) for i, row in enumerate(img2) for j, item in enumerate(row) if item]
        counter = Counter((ax - bx, ay - by) for ax, ay in A for bx, by in B)
        return max(counter.values() or (0,)) 
