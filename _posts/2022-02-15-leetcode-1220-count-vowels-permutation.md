---
layout      : single
title       : LeetCode 1220. Count Vowels Permutation
tags 		: LeetCode Hard DP
---
DP教學系列。當初解這題時還跟朋友討論得好開心，他還想出非常變態的解法，請務必看看[他的文章](https://medium.com/cow-say/1220-count-vowels-permutation-921d259e9439)。

# 題目
輸入整數n，計算出符合以下規則的長度n字串有多少種。答案很大，需要模10^9+7  
- 字串只出現小寫母音aeiou
- a後面只會出現e
- e後面只會出現a,i
- i後面**不會**出現i
- o後面只會出現i,u
- u後面只會出現a

# 解法
>步驟1：定義狀態  

變數有長度，以及結尾的五個字母，使用二維DP。  
因為有五個字母，就由0~4依序表示aeiou。dp[i][0]表示字串長度i時由a結尾的數量。

>步驟2：找出狀態轉移方程式  

題目講一大串誰後面只會出現誰，看得不太好理解，先把它全部列出來。發現反過來講意思其實可以理解成： 
- 在所有的eiu後面加上a
- 在所有的ai後面加上e
- 在所有的eo後面加上i
- 在所有的i後面加上o
- 在所有的io後面加上u

推出轉移方程式：  
- dp[i][0]=dp[i-1][1]+dp[i-1][2]+dp[i-1][4]
- dp[i][1]=dp[i-1][0]+dp[i-1][2]
- dp[i][2]=dp[i-1][1]+dp[i-1][3]
- dp[i][3]=dp[i-1][2]
- dp[i][4]=dp[i-1][2]+dp[i-1][3]

>步驟3：處理base cases

沒有長度為-1的字串，為避免錯誤，直接將dp[i]的所有元素初始化為1，對應初始的a,e,i,o,u字串。

最後dp[-1]加總起來就是總數，模運算後得到正確答案。

```python
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[1]*5 for _ in range(n)]
        MOD = 10**9+7

        for i in range(1, n):
            dp[i][0] = (dp[i-1][1]+dp[i-1][2]+dp[i-1][4]) % MOD
            dp[i][1] = (dp[i-1][0]+dp[i-1][2]) % MOD
            dp[i][2] = (dp[i-1][1]+dp[i-1][3]) % MOD
            dp[i][3] = (dp[i-1][2]) % MOD
            dp[i][4] = (dp[i-1][2]+dp[i-1][3]) % MOD

        return sum(dp[-1]) % MOD
```

但是誰能一下子看懂dp[0]代表什麼鬼？  
直接用變數命名更加直觀。又因為python的特性，可以同時賦予多個變數值，可以簡化成以下程式碼，可讀性更高。
查了下這功能叫做parallel assignment，有點類似JS中的解構賦值。

```python
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a = e = i = o = u = 1
        for _ in range(n-1):
            a, e, i, o, u = e+i+u, a+i, e+o, i, i+o
        return (a+e+i+o+u) % (10**9+7)
```

還有一種解法，結合矩陣運算以及快速乘冪，效率超過了100%的提交。  
詳見[朋友文章](https://medium.com/cow-say/1220-count-vowels-permutation-921d259e9439)。
