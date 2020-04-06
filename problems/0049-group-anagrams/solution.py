from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        groups = defaultdict(list)
        for s in strs: 
            key = {i: 0 for i in string.ascii_lowercase}
            for ch in s: key[ch] += 1
            groups[tuple(key.values())].append(s)
        return groups.values()
