import string
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        alpha_num_map = dict(zip(string.ascii_uppercase, range(1, 27)))
        column_num = 0
        multiple = 1
        for i in reversed(s):
            column_num += alpha_num_map[i] * multiple
            multiple *= 26
        
        return column_num
