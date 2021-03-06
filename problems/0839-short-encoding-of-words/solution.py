class TrieNode:
    
    def __init__(self, val, is_end=False, children=None):
        self.val = val
        self.is_end = is_end
        self.children = children if children else {}


class Solution:
    def make_trie(self, words):
        def insert_to_trie(trie, word):
            for ch in word:
                if ch not in trie.children:
                    trie.children[ch] = TrieNode(ch)
                trie = trie.children[ch]
            trie.is_end = True

        trie = TrieNode('#')
        for word in words: insert_to_trie(trie, word)
        return trie
    
    def count_nodes_in_tree(self, root: TrieNode, depth=0) -> int:
        if not root.children: return depth + 1
        return sum(map(lambda node: self.count_nodes_in_tree(node, depth + 1), root.children.values()))
    
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = self.make_trie(map(reversed, words))
        return self.count_nodes_in_tree(trie)
