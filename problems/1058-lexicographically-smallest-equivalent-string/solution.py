from collections.abc import *

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, base_str: str) -> str:
        charset = string.ascii_lowercase

        dsu = LexicoDSU(charset)
        for u, v in zip(s1, s2): dsu.union(u, v)

        return "".join(map(dsu.find, base_str))

class LexicoDSU:
    """A DSU implementation which maintains the lexicographically smaller element of the disjoint-set as root"""
    T = Hashable

    def __init__(self, xs: Iterable[T] = tuple()) -> None:
        self.parents = {x: x for x in xs}
    
    def add(self, x: T) -> None:
        if x in self.parents: return
        self.parents[x] = x
    
    def make_safe(func: Callable) -> Callable:
        def wrapper(self, *xs):
            for x in xs: self.add(x)
            return func(self, *xs)
        return wrapper
    
    @make_safe
    def union(self, u: T, v: T) -> None:
        ur, vr = self.find(u), self.find(v)
        small, large = (ur, vr) if ur < vr else (vr, ur)
        self.parents[large] = small
    
    @make_safe
    def find(self, x: T) -> T:
        self.parents[x] = self.find(self.parents[x]) if self.parents[x] != x else x
        return self.parents[x]
    
    @make_safe
    def is_connected(self, u: T, v: T) -> bool:
        return self.find(u) == self.find(v)
