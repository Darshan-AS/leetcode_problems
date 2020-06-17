class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old_color = image[sr][sc]
        if newColor == old_color:
            return image
        
        def is_valid(i, j):
            return True if 0  <= i < len(image) and 0 <= j < len(image[0]) else False
        
        def fill(x, y):
            if image[x][y] == old_color:
                image[x][y] = newColor
                for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    if is_valid(x + i, y + j):
                        fill(x + i, y + j)
        fill(sr, sc)
        return image
    
    def is_valid(self, image, i, j):
        return True if 0  <= i < len(image) and 0 <= j < len(image[0]) else False
