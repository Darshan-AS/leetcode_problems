class Solution:
    def wordBreak(self, s: str, words: List[str]) -> List[str]:
        trie = Trie(words)        
        n = len(s)
        
        dp = [[] for _ in range (n + 1)]
        dp[0] = ['']
        
        for j in range(1, n + 1):
            dp[j] = list(chain.from_iterable(
                (p + ' ' + s[i:j] if p else s[i:j] for p in dp[i])
                for i in range(j)
                if trie.search(s[i:j])
            ))
        
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
