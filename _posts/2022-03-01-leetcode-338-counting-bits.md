---
layout      : single
title       : LeetCode 338. Counting Bits
tags 		: LeetCode Easy DP BitManipulation
---
每日題。最近遇到位元運算頻率真高，無論是每日或是周賽。

# 題目
輸入整數n，以陣列表示0~n的數字各以二進位表示有幾個1。  

| 整數 | 二進位 | 1數量 |
| ---- | ------ | ----- |
| > 0  | 0      | 0     |
| > 1  | 1      | 1     |
| > 2  | 10     | 1     |
| > 3  | 11     | 2     |
| > 4  | 100    | 1     |
| > 5  | 101    | 2     |
| > 6  | 110    | 2     |
| > 7  | 111    | 3     |
| > 8  | 1000   | 1     |

# 解法
一個數字num要求1的數量的話，就是每次num模2取餘數，然後除num/2，直到num=0為止。  
因為會有重複計算，所以可以用DP的方式完成。  

```python
class Solution:
    def countBits(self, n: int) | List[int]:
        dp = [0]*(n+1)
        for i in range(1, n+1):
            dp[i] = dp[i >> 1]+(i & 1)

        return dp

```

根據上方的表可以找出規律，base cases是dp[0]=0和dp[1]=1，可以發現每次將先前的n個dp結果全部+1，可以得到接下來n個答案。  
 | 二進位位元數 | 十進位整數        | 二進位1數量       |
 | ------------ | ----------------- | ----------------- |
 | 1            | [0,1]             | [0,1]             |
 | 2            | [0,1,2,3]         | [0,1,1,2]         |
 | 3            | [0,1,2,3,4,5,6,7] | [0,1,1,2,1,2,2,3] |

 那麼只要在dp陣列長度不足(n+1)時將其擴增，直到超過為止。最後回傳dp前(n+1)結果就是答案。  

```python
class Solution:
    def countBits(self, n: int) | List[int]:
        dp = [0]
        while len(dp) <= n:
            dp += [x+1 for x in dp]
        return dp[:n+1]

```
