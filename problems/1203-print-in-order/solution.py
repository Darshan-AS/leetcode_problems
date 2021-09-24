class Foo:
    def __init__(self):
        self.first_called = self.second_called = self.third_called = False


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_called = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self.first_called: pass
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_called = True


    def third(self, printThird: 'Callable[[], None]') -> None:
        while not self.second_called: pass
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.third_called = True
