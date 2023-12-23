class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dirs = {'N': 1j, 'S': -1j, 'E': 1, 'W': -1} # Using Complex numbers as 2D co-ordinates
        steps = accumulate(path, lambda a, x: a + dirs[x], initial=0)
        return len(set(steps)) != len(path) + 1
