class Solution:
    def minOperations(self, logs: List[str]) -> int:
        def cd(depth: int, log: str) -> int:
            if log == '../': return max(depth - 1, 0)
            elif log == './': return depth
            else: return depth + 1
        
        return reduce(cd, logs, 0)
