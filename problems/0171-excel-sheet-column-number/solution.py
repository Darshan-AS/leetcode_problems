import string
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        alpha_num_map = dict(zip(string.ascii_uppercase, range(1, 27)))
        column_num = 0
        for i in s:
            column_num = column_num * 26 + alpha_num_map[i]
        
        return column_num
