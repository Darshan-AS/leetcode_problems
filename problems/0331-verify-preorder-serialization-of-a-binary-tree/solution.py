class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        spaces = 1
        for ch in preorder.split(','):
            if spaces <= 0:
                return False
            spaces += 1 if ch != '#' else -1
 
        return spaces == 0
