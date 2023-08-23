class Solution:
    def convertToTitle(self, column_number: int) -> str:
        solution_values = []
        i = column_number
        
        while i:
            i = i - 1
            solution_values.append(chr(ord('A') + (i % 26)))
            i = i // 26
        
        return ''.join(reversed(solution_values))
