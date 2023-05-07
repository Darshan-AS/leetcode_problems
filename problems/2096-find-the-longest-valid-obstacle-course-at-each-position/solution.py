class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
        lis = []
        ans = []
        for x in obstacles:
            if not lis or lis[-1] <= x: lis.append(x); ans.append(len(lis))
            else: lis[(k := bisect_right(lis, x))] = x; ans.append(k + 1)
        return ans
