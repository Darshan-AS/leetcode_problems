class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        telephone_map = {
            1: ''    , 2: 'abc', 3: 'def',
            4: 'ghi' , 5: 'jkl', 6: 'mno',
            7: 'pqrs', 8: 'tuv', 9: 'wxyz'
        }
        
        combs = ['']
        for d in digits:
            combs = [c + ch for c in combs for ch in telephone_map[int(d)]]
        
        return combs if digits else []
