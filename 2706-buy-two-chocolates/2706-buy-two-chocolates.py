class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        min_1=float('inf')
        min_2=float('inf')
        for i in range(0,len(prices)):
            if prices[i]<min_1:
                min_1,min_2=prices[i],min_1
            elif prices[i]<min_2:
                min_2=prices[i]
        return money-(min_1+min_2) if (money-(min_1+min_2))>=0 else money
