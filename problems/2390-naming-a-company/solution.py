class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        groups = defaultdict(set)
        for idea in ideas: groups[idea[0]].add(hash(idea[1:]))
        
        return sum(
            (len(ga) - len(gab)) * (len(gb) - len(gab))
            for ga, gb in combinations_with_replacement(groups.values(), 2)
            for gab in (ga & gb,)
        ) * 2
        
