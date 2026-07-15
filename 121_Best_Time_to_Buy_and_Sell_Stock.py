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

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, sell = 0, 1
        maxProfit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                maxProfit = max(maxProfit, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        
        return maxProfit