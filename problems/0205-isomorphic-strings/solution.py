class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """        
        for _ in range(2):
            hash_map = {}
            
            for i, j in zip(s, t):
                if i in hash_map.keys() and hash_map[i] != j:
                    return False
                hash_map[i] = j
            s, t = t, s
        return True
