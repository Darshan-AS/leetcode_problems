class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        i = len(self.stocks) - 1
        ans = 1
        while i >= 0:
            if self.stocks[i][0] > price:
                break
            
            ans += self.stocks[i][1]
            i -= self.stocks[i][1]
        
        self.stocks.append((price, ans))
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
