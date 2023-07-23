--- 
layout      : single
title       : LeetCode 2787. Ways to Express an Integer as Sum of Powers
tags        : LeetCode Medium Array DP
---
雙周賽109。還是dp，測資範圍很奇怪，總感覺有奇怪的地雷，害我擔心很久。  
雖然我是沒有踩中，但是理論上不重複的測資只有300\*5種，官方卻搞了1502組，不知道存什麼心。  

另外小抱怨一下，這次周賽Q3和Q4給的參數x和n都卡到我常用變數名稱，python重複宣告又不會出錯，浪費好多時間debug。  

# 題目
輸入兩個**正整數**n和x。  

求將n拆成數個**不重複**正整數的x次方總和，共有幾種方法。  
也就是說，找到某些不同的整數[n<sub>1</sub>, n<sub>2</sub>,... ,n<sub>k</sub>]，滿足n = [n<sub>1</sub><sup>x</sup>, n<sub>2</sub><sup>x</sup>,... ,n<sub>k</sub><sup>x</sup>]。  

例如n = 160, x = 3，其中一種方法是n = 2<sup>3</sup>+3<sup>3</sup>+5<sup>3</sup>。  

答案可能很大，先模10^9+7後回傳。  

# 解法
如果x越大，某數a的x次方能組成n機率越小。  
最差的情況下x=1，那麼n有可以由1\~n的所有數字來組成，那麼先篩出所有可能的數nums。  

我們只在乎選了哪些數，不在乎順序。也就是決定nums中的數**選或不選**，總和正好等於n的方法有幾種。  
其實就是經典的01背包問題。  

時間複雜度O(n^2)。  
空間複雜度O(n^2)。  

```python
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD=10**9+7
        nums=[i**x for i in range(1,n+1) if i**x<=n]
        
        N=len(nums)
        dp=[[0]*(n+1) for _ in range(N+1)]
        dp[0][0]=1
        
        for i in range(1,N+1):
            val=nums[i-1]
            for j in range(n+1):
                dp[i][j]=dp[i-1][j]
                if j>=val:
                    dp[i][j]+=dp[i-1][j-val]
                    dp[i][j]%=MOD
                    
        return dp[N][n]
```

比賽中我直接寫出了空間優化的方法，還是挺開心的。  

時間複雜度O(n^2)。  
空間複雜度O(n)。  

```python
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD=10**9+7
        nums=[i**x for i in range(1,n+1) if i**x<=n]
        
        dp=[0]*(n+1)
        dp[0]=1
        for val in nums:
            for j in reversed(range(val,n+1)):
                dp[j]+=dp[j-val]
                dp[j]%=MOD
                
        return dp[n]
```