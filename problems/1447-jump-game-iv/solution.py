class Solution:
    def minJumps(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3: return n - 1
        
        indexes = defaultdict(deque)
        for i, x in enumerate(nums): indexes[x].appendleft(i)

        queue = deque(((0, 0),))
        seen = {0}
        while queue:
            i, c = queue.popleft()
            for j in chain(indexes[nums[i]], (i + 1, i - 1)):
                if j < 0 or j >= n or j in seen: continue
                if j == n - 1: return c + 1
                seen.add(j)
                queue.append((j, c + 1))
            indexes[nums[i]].clear()
            
        return n - 1
        
