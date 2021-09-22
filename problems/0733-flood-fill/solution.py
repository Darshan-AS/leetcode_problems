class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        old_color = image[sr][sc]
        new_image = deepcopy(image)
        m, n = len(new_image), len(new_image[0])
        
        if new_color == old_color:
            return new_image
        
        queue = collections.deque([(sr, sc)])
        while queue:
            r, c = queue.popleft()
            new_image[r][c] = new_color
            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                if 0 <= r + dr < m and 0 <= c + dc < n and new_image[r + dr][c + dc] == old_color:
                    queue.append((r + dr, c + dc))
        
        return new_image
