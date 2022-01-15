from sortedcontainers import SortedDict

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        sd = SortedDict()
        
        sd[arr[-1]] = (True, True) # (can_odd_jump, can_even_jump)
        sd[-math.inf] = sd[math.inf] = (False, False)
        
        count = 1
        for i in range(n - 2, -1, -1):
            x = arr[i]
            ge_x = sd.keys()[sd.bisect_left(arr[i])]
            le_x = sd.keys()[sd.bisect_right(arr[i]) - 1]

            can_odd_jump, can_even_jump = sd[ge_x][1], sd[le_x][0]
            sd[x] = (can_odd_jump, can_even_jump)
            count += can_odd_jump
            
        return count
