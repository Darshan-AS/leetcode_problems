class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        
        for i, ch in enumerate(strs[0]):
            for s in strs[1:]:
                if i == len(s) or ch != s[i]:
                    return s[:i]
        return strs[0]
