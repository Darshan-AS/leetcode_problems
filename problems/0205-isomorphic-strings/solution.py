class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_map, t_map = {}, {}
        
        for i, j in zip(s, t):
            if (i in s_map.keys() and s_map[i] != j) or (j in t_map.keys() and t_map[j] != i):
                return False
            s_map[i], t_map[j] = j, i
        return True
