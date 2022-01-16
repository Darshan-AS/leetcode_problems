# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def match_count(word1: str, word2: str) -> int:
            return sum(map(operator.eq, word1, word2))
        
        words = tuple(wordlist)
        guess_match_count = 0
        while guess_match_count != 6:
            guess_word = random.choice(words)
            guess_match_count = master.guess(guess_word)
            words = tuple(filter(lambda word: match_count(word, guess_word) == guess_match_count, words))
