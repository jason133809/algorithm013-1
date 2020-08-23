class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0 
        for i in range(1,len(prices)):#循环遍历整个数组
            if prices[i] > prices[i-1]:#比较当前与前一个元素的值
                profit += prices[i]-prices[i-1] #如果当前值比它之前的值大就相减并累加求和
        return profit