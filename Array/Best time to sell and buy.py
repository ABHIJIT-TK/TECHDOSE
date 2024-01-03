    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        a=0
        while r<len(prices):
            if prices[r]>prices[l]:
                profit=prices[r]-prices[l]
                if profit>a:
                    a=profit
            else:
                l=r
            r+=1
        return a
