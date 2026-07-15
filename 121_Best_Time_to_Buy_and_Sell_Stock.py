class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        
        maxProfit = 0

        for buy in range(n): 
            bestSell = 0
            for sell in range(buy + 1, n):
                if sell < bestSell:
                    continue
                
                bestSell = sell
                maxProfit = max(prices[sell] - prices[buy], maxProfit)
                

        return maxProfit