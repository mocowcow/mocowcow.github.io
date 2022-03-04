---
layout      : single
title       : LeetCode 799. Champagne Tower
tags 		: LeetCode Medium DP
---
每日題。自昨天知道臭狗有心臟病，到現在還是很難過。

# 題目
以玻璃杯堆成香檳塔，第一層有1杯，第二層2杯，以此類推，總共有100層。  
每個杯子最多可以裝1的容量，多餘的會往左下和右下兩杯平均流入。  
從頂端倒入poured杯的的酒量，求第query_row層左邊數來第query_glass杯有多少酒。  

# 解法
其實有點像是巴斯卡三角形，與其當作正三角形，不如當直角三角形來看待更好計算。  
剛開始走了彎路，想著計算每一杯是由上層杯子流入，做了不少多餘的計算。  
定義dp(r,c)為第r層第c的的酒量。因為是由上層一或二杯溢出後而成，dp(r,c)=(r-1,c)溢出一半+(r-1,c-1)溢出的一半。  
當c=0時為base case，因沒有左上方的杯子，所以只取正上方溢出的一半；最右邊的杯子的右上方會直接當作0，不需理會。  
杯子最多只能裝1，所以答案要記得跟1取最小。

```python
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0]*100 for _ in range(100)]
        dp[0][0] = poured
        for r in range(1, query_row+1):
            for c in range(r+1):
                if c == 0:
                    dp[r][0] = max(0, (dp[r-1][0]-1))/2
                else:
                    dp[r][c] = max(0, (dp[r-1][c]-1))/2 + max(0, (dp[r-1][c-1]-1))/2

        return min(1, dp[query_row][query_glass])

```

看別人解法才想到把每杯溢出的往下加更有效率，省得在那邊取max。  
因為要往下層做運算，所以dp空間要多開一格，不然會出錯。

```python
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0]*101 for _ in range(101)]
        dp[0][0] = poured
        for r in range(query_row+1):
            for c in range(r+1):
                overflow = (dp[r][c]-1)/2
                if overflow > 0:
                    dp[r+1][c] += overflow
                    dp[r+1][c+1] += overflow

        return min(1, dp[query_row][query_glass])

```
