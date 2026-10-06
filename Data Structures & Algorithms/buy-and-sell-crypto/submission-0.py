class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #choose one day rn to buy and a different day to sell, has to be in teh future
        #return max profit, can also choose not to make any transactions

        #keep track of min price as you go through the array
        #if today's price is cheaper than min price then update becaus eyou'd rather buy today
        #check ho wmuch profit you'd make if you sold today, today's price.- min_price. if bigger than max_profit, update max_profit
        n=len(prices)
        min_price=10**19
        max_profit=0
        for i in range(n):
            if prices[i]<min_price:
                min_price=prices[i]
            else:
                profit=prices[i]-min_price
                if profit>max_profit:
                    max_profit=profit
        return max_profit