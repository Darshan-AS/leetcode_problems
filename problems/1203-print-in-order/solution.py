class Foo:
    def __init__(self):
        self.n = 1

    def first(self, printFirst: 'Callable[[], None]') -> None:
        while self.n != 1: pass
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.n = 2

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.n != 2: pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.n = 3

    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.n != 3: pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.n = 1
        
