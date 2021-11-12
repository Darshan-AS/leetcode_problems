class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        telephone_map = {
            1: ''    , 2: 'abc', 3: 'def',
            4: 'ghi' , 5: 'jkl', 6: 'mno',
            7: 'pqrs', 8: 'tuv', 9: 'wxyz'
        }
        
        def letter_combs(index, comb):
            if index == len(digits):
                yield ''.join(comb)
                return
            
            for ch in telephone_map[int(digits[index])]:
                comb.append(ch)
                yield from letter_combs(index + 1, comb)
                comb.pop()
        
        return list(letter_combs(0, [])) if digits else []
