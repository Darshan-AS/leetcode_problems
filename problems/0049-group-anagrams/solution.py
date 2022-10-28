class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for s in strs: 
            key = frozenset(Counter(s).items())
            groups[key].append(s)
        return groups.values()
