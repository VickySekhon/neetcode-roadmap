class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        # max_profit = 0
        # j, i = 0, 1
        # while i < len(prices):
        #   future_price = prices[i]
        #   today_price = prices[j]
        #   profit = future_price - today_price
        #   if profit > max_profit:
        #       max_profit = profit
        #       i+=1
        #   if profit < 0:
        #       j += 1
        # return max_profit

        # max_profit = 0
        # j = 0
        # for future_price in prices[1:]:
        #     today_price = prices[j]
        #     profit = future_price - today_price
        #     if profit > max_profit:
        #         max_profit = profit
        #     if profit < 0:
        #         j += 1
        # return max_profit
        
        max_profit, j = 0, 0
        for indx, future_price in enumerate(prices[1:], 1):
            today_price = prices[j]
            profit = future_price - today_price
            if profit <= 0:
                j = indx
            elif profit > max_profit:
                max_profit = profit
        return max_profit
   

sol = Solution()
x = sol.maxProfit(prices=[2,1,2,1,0,1,2])
print(x)

""" 
[2,1,2,1,0,1,2]
         j   i

[2,1,2,1,0,1,2]
   j   i
   
[2,1,2,1,0,1,2]
     j   i
     
[2,1,2,1,0,1,2]
       j   i


"""