class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # Reuse from word break problem
        def word_break(s: str, words_set: set[str]) -> bool:
            @cache
            def dfs(k: int) -> bool:
                return any(s[i:k] in words_set and dfs(i) for i in range(k)) if k else True

            return dfs(len(s))
        
        words_set = set(words)
        concat_words = []
        
        for word in words:
            words_set.remove(word)
            if word and word_break(word, words_set): concat_words.append(word)
            words_set.add(word)
        
        return concat_words
