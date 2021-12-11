class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def add(s: set, x: Any) -> set:
            s.add(x)
            return s
        
        def can_reach(index: int, seen: set) -> bool:
            return (
                arr[index] == 0 or 
                can_reach(index + arr[index], add(seen, index)) or 
                can_reach(index - arr[index], add(seen, index))
                if 0 <= index < len(arr) and index not in seen
                else False
            )
        
        return can_reach(start, set())
