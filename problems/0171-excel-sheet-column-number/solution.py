import string
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        column_num = 0
        for i in s:
            column_num = column_num * 26 + ord(i) - ord('A') + 1
        
        return column_num
