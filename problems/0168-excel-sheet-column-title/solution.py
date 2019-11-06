import string
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        alpha_value_map = dict(zip(range(26), string.ascii_uppercase))
        
        solution_values = []
        i = n
        
        if i <= 26:
            return alpha_value_map[i - 1]
        
        while i:
            i -= 1
            solution_values.append(alpha_value_map[(i % 26)])
            i = i // 26
        
        return ''.join(reversed(solution_values))
