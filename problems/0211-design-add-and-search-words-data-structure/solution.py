class Node:

    def __init__(self, ch=None, is_end=False):
        self.ch = ch
        self.is_end = is_end
        self.children = {}


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_root = Node()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.trie_root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node(ch)
            curr = curr.children[ch]
        curr.is_end = True

    def search(self, word: str, root=None) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        curr = self.trie_root if root is None else root
        for i in range(len(word)):
            if word[i] == '.':
                return any(map(lambda v: self.search(word[i + 1:], v), curr.children.values()))
            if word[i] not in curr.children:
                return False
            curr = curr.children[word[i]]
        return curr.is_end

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
