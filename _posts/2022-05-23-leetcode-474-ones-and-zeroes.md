--- 
layout      : single
title       : LeetCode 474. Ones and Zeroes
tags        : LeetCode Medium Array String DP
---
每日題。0/1背包問題變形，差點忘記bottom up怎麼寫。

# 題目
輸入一個二進位字串陣列strs和兩個整數m, n。
回傳strs的最大子集合的大小，且子集合中最多只有m個0和n個1。

# 解法
對於每個二進位字串strs[i]可以選擇拿或不拿，拿了就扣掉容量，並計數+1。  
和原本的0/1背包不同的唯一差別，就是容量變成兩種，要兩種都裝得下才可以拿。  

先建立兩個陣列zeros和ones，計算每個字串strs[i]所包含的0與1數量。  
定義dp(i,zero,one)：代表當前處理strs[i]，且還可以使用zero個0與one個1，並回傳最大子集合大小。  
轉移方程式：dp(i,zero,one)=max(dp(i-1,zero,on), dp(i-1,zero-zeros[i],one-ones[i]))  
base cases：當zero或one小於0，代表超出數量限制，回傳-inf使該答案不會被使用；i<0時，代表所有字串都被處理過，回傳0。  

回傳dp(N-1,m,n)就是答案。

```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        N=len(strs)
        zeros=[x.count('0') for x in strs]
        ones=[x.count('1') for x in strs]
        
        @cache
        def dp(i,zero,one):
            if zero<0 or one<0:
                return -math.inf
            if i<0:
                return 0
            return max(dp(i-1,zero,one),dp(i-1,zero-zeros[i],one-ones[i])+1)
                    
        return dp(N-1,m,n)
```

top down方法計算了太多不會碰到的狀態，過於浪費記憶體。  
其實遍歷每個strs[i]，只會參考到strs[i-1]的狀態，改成bottom up將空間壓縮到O(m*n)。  

遍歷每個strs[k]，計算出共有zeros個0以及ones個1，並由i=m\~0, j=n\~0的順序反向更新dp值。  
如果是循序更新的話，每個字串strs[k]會被重複使用不只一次，得到錯誤結果。

```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp=[[0]*(n+1) for _ in range(m+1)]
        
        for s in strs:
            zeros=s.count('0')
            ones=s.count('1')
            for i in reversed(range(zeros,m+1)):
                for j in reversed(range(ones,n+1)):
                    dp[i][j]=max(dp[i][j],dp[i-zeros][j-ones]+1)
        
        return dp[-1][-1]
```
