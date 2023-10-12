# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, m_arr: 'MountainArray') -> int:
        MountainArray.__getitem__ = MountainArray.get
        MountainArray.__len__ = MountainArray.length

        n = len(m_arr)
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            l, r = (m + 1, r) if m_arr[m] < m_arr[m + 1] else (l, m)
        p = l

        a = bisect_left(m_arr, target, hi=p + 1)
        if a < n and m_arr[a] == target: return a

        b = bisect_left(m_arr, -target, lo=p + 1, key=neg)
        if b < n and m_arr[b] == target: return b

        print(p, a, b)
        return -1
