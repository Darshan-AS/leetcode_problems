class Solution:
    def toGoatLatin(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        
        def to_goat_latin_word(index_word):
            index, word = index_word
            goat_word = word if word[0] in vowels else word[1:] + word[0]
            return goat_word + "ma" + "a" * (index + 1)
        
        return ' '.join(map(to_goat_latin_word, enumerate(s.split())))
