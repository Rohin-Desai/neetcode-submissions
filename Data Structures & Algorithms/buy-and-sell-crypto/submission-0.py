class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minV = float('inf')
        n = len(prices)
        l = 0
        profit = 0
        for i in range(1,n+1):
            #incoming cell we see if selling will result in 
            #profit at the cells index.
            if minV < prices[i-1]:
                profit = max(prices[i-1] - minV, profit)
            #Now cell part of window, we update the min 
            #value of the window. 
            minV = min(minV,prices[i-1])
        return profit
        