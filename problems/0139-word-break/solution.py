class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        trie = Trie(words)        
        n = len(s)
        
        dp = [False] * (n + 1)
        dp[0] = True
        
        for j in range(1, n + 1):
            dp[j] = any(dp[i] and trie.search(s[i:j]) for i in range(j))
        
        return dp[-1]


class TrieNode:
    def __init__(self, children: dict = None, is_end: bool = False) -> None:
        self.children = children if children else defaultdict(TrieNode)
        self.is_end = is_end


class Trie:
    def __init__(self, words: list[str]) -> None:
        self.root = TrieNode()
        for word in words: self.insert(word)

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
