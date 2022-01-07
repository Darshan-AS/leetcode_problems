class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        name_counters = defaultdict(lambda: itertools.count(1))
        seen_names = set()
        
        new_names = []
        for name in names:
            new_name = name
            while new_name in seen_names:
                new_name = f'{name}({next(name_counters[name])})'
                
            new_names.append(new_name)
            seen_names.add(new_name)
        
        return new_names
