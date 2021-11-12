class Solution:
    def letterCombinations(self, digits_: str) -> List[str]:
        telephone_map = {
            1: ''    , 2: 'abc', 3: 'def',
            4: 'ghi' , 5: 'jkl', 6: 'mno',
            7: 'pqrs', 8: 'tuv', 9: 'wxyz'
        }
        
        def letter_combs(digits):
            yield from (
                ch + c
                for c in letter_combs(digits[1:])
                for ch in telephone_map[int(digits[0])]
            ) if digits else ('',)
        
        return list(letter_combs(digits_)) if digits_ else []
