class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,0
        profit = 0
        for i in range(1,len(prices)):
            if prices[r] < prices[l]:
                l = r         
            if prices[i] < prices[r]:
                profit += prices[r] - prices[l]
                l = i 
            r += 1 
        profit += prices[r] - prices[l]
        return profit
        