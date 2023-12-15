class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        return (set((b for _, b in paths)) - set(a for a, _ in paths)).pop()
        
