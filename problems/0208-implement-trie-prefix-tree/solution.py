class Trie:
    
    class Node:
        def __init__(self, children: dict = None, is_end: bool = False) -> None:
            self.children = children if children else defaultdict(Trie.Node)
            self.is_end = is_end

    def __init__(self) -> None:
        self.root = Trie.Node()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word: node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children: return False
            node = node.children[ch]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children: return False
            node = node.children[ch]
        return True
    

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
