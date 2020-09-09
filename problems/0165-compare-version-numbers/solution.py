from functools import reduce

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def weight(version):
            ans = list(map(int, version.split('.')))
            while ans and not ans[-1]: ans.pop()
            return ans
        
        v1, v2 = weight(version1), weight(version2)
        if v1 > v2: return 1
        elif v1 < v2: return -1
        else: return 0
