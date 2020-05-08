class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        if len(c) <= 2:
            return True
        
        y = (c[1][1] - c[0][1])
        x = (c[1][0] - c[0][0])
        for i in range(1, len(c)):
            if x * (c[i][1] - c[i - 1][1]) != y * (c[i][0] - c[i - 1][0]):
                return False
        return True
