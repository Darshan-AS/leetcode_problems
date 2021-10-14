class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        
        def visit_province_from(city: int):
            visited.add(city)
            for neighbouring_city in filter(lambda i: isConnected[city][i] and i not in visited, range(n)):
                visit_province_from(neighbouring_city)
        
        province_count = 0
        for city in range(n):
            if city not in visited:
                visit_province_from(city)
                province_count += 1
        
        return province_count
