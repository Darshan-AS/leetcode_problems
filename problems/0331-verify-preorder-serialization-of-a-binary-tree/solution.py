class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        spaces = 1 # Number of empty spots
        for ch in preorder.split(','):
            if spaces <= 0:
                return False
            spaces += 1 if ch != '#' else -1 # Non '#' char uses 1 empty space and produces 2. '#' uses 1
 
        return spaces == 0
