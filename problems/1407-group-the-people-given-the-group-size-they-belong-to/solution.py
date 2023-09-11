class Solution:
    def groupThePeople(self, group_sizes: list[int]) -> list[list[int]]:
        groups = defaultdict(lambda: [[]])
        for i, s in enumerate(group_sizes):
            if len(groups[s][-1]) == s: groups[s].append([])
            groups[s][-1].append(i)
        
        return list(chain.from_iterable(groups.values()))

