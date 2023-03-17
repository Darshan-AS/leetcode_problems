class Trie:

    class Node:
        def __init__(self, children: dict = None, is_end: bool = False) -> None:
            self.children = defaultdict(Trie.Node) if children is None else children
            self.is_end = is_end

    f = lambda a, x: a.children[x]
    g = lambda a, x: x not in a.children

    def __init__(self):
        self.root = Trie.Node()

    def insert(self, word: str) -> None:
        reduceM(Trie.f, word, self.root).is_end = True

    def search(self, word: str) -> bool:
        return (n := reduceM(Trie.f, word, self.root, Trie.g)) is not None and n.is_end

    def startsWith(self, prefix: str) -> bool:
        return reduceM(Trie.f, prefix, self.root, Trie.g)


T = TypeVar('T')
A = TypeVar('A')
Mapper = Callable[[A, T], A]
Predicate  = Callable[[A, T], bool]

def reduceM(f: Mapper, xs: Iterable[T], init: A | None = None, g: Predicate = lambda *_: False) -> A | None:
    """Similar to functools.reduce, but terminates early if the predicate g(_, _) is True"""
    xs = iter(xs)
    a = next(xs) if init is None else init
    for x in xs:
        if g(a, x): return
        a = f(a, x)
    return a

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
