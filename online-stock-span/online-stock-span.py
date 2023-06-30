class StockSpanner:

    def __init__(self):
        self.stack = []
        self.span = {}
        

    def next(self, price: int) -> int:
        # maintain a monotonically decreasing stack that stores the stock's price. If today's stock price is greater than yesterday's, then pop the previous day's price from the stack (repeatedly) and add it's span (stored in a hashmap), store <today, new span> in hashmap and delete <previous, old span> from hashmap. Return this span as the answer.
        span_value = 1
        while (len(self.stack) != 0) and price >= self.stack[-1]:
            span_value += self.span[self.stack[-1]]
            del self.span[self.stack[-1]]
            self.stack.pop()
        self.stack.append(price)
        self.span[price] = span_value
        return span_value
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)