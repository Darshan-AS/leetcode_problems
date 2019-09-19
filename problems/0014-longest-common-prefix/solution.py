class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i, ch in enumerate(strs[0]):
            for j in strs[1:]:
                if i == len(j) or ch != j[i]:
                    return strs[0][:i]
        return strs[0]
