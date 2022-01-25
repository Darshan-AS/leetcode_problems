class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def common_prefix(s1: str, s2: str) -> str:
            return ''.join(takewhile(
                bool,
                map(lambda x, y: x if x == y else '', s1, s2),
            ))
        
        return reduce(common_prefix, strs)
