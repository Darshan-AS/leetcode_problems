import string
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        solution_values = []
        i = n
        
        while i:
            i = i - 1
            solution_values.append(chr(ord('A') + (i % 26)))
            i = i // 26
        
        return ''.join(reversed(solution_values))
