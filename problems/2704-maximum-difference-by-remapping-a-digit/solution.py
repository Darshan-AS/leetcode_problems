class Solution:
    def minMaxDifference(self, num: int) -> int:
        s_num = str(num)

        ch = s_num[0]
        min_num = int(s_num.replace(ch, '0'))

        ch = next((x for x in s_num if x != '9'), '0')
        max_num = int(s_num.replace(ch, '9'))

        return max_num - min_num
