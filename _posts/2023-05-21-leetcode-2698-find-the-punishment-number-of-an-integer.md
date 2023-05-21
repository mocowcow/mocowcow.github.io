--- 
layout      : single
title       : LeetCode 2698. Find the Punishment Number of an Integer
tags        : LeetCode Medium Backtracking
---
周賽346。

# 題目
輸入正整數n，回傳n的**懲罰數**。  

一個數字n的**懲罰數**為所有滿足以下條件的i的平方和：  
- 1 <= i <= n  
- 將i\*i以字串表示後分割成若干個子字串，且子字串對應的整數和等於i  

# 解法
這題還挺妙的，不太像是傳統的回溯題，仔細算了下才確定可以。  
n最大1000，所以i最大也是1000，平方後10^6，也就是7位數字。  
窮舉i\*i每個點**分割**或**不分割**，最多有2^7=128種可能，只要任一種方案總和等於i，則代表會對**懲罰數**做出貢獻。  

最後逐一檢查1\~n中有哪些數字符合規則，並將其平方值加入答案。  

時間複雜度O(n \* 2^(log n^2))，大概是1000\*128次計算。  
空間複雜度O(log n^2)。  

```python
class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def ok(n):
            s=str(n*n)
            def dfs(i,curr,sm):
                if i==len(s):
                    return sm+curr==n
                x=int(s[i])
                if dfs(i+1,curr*10+x,sm):
                    return True
                if dfs(i+1,x,sm+curr):
                    return True
                return False
            
            return dfs(0,0,0)
        
        ans=0
        for i in range(1,n+1):
            if ok(i):
                ans+=i*i
                
        return ans
```
