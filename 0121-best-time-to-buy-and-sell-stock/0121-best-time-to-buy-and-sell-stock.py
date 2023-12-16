class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = prices[0],0
        profit = 0
        for price in prices:
            if price < l:
                l = price
                r = 0
            else:
                if price > r:
                    r = price
                if profit < r - l:
                    profit = r - l
        
        return profit