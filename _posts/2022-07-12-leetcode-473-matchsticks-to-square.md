--- 
layout      : single
title       : LeetCode 473. Matchsticks to Square
tags        : LeetCode Medium Array Backtracking
---
每日題。一看就知道是回溯，但比起以前新增了許多測資，需要更佳的剪枝才能AC。  

# 題目
輸入整數陣列matchsticks，其中matchsticks[i]代表第i根火柴的長度。你必須在不破壞火柴的情況下組成一個正方形，且每一根火柴都必須使用到。  
若可以組成正方形則回傳ture，否則回傳false。

# 解法
題目只問能不能組成正方形，而不管使用的順序或是位置，那麼火柴放在哪其實都可以。  
首先過排除幾個明顯不可能的情況：  
- 火柴不足4根  
- 總長度無法公平分配給4個邊  
- 最長的火柴超過所需邊長  

接下來只要試著把所有火柴塞到某個邊裡面了。  
先從最長的火柴開始塞，可以有效降低後續的分支數量，故先將火柴以遞減排序。  

bt(i)代表當前正試著放入第i根火柴，當i等於N時代表所有火柴已放置完成，回傳true；否則試著將火柴i塞入四個邊裡面。  
這裡有個非常重要的剪枝：  
若第j個邊與第j-1個邊現有長度相同，則略過嘗試，因為不管塞在哪邊結果都是一樣的。  

```python
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        N=len(matchsticks)
        sm=sum(matchsticks)
        matchsticks.sort(reverse=True)
        length=sm//4
        if N<4:return False
        if sm%4!=0:return False
        if matchsticks[0]>length:return False
        
        side=[0]*4
        
        def bt(i):
            if i==N:
                return True
            for j in range(4):
                if j>0 and side[j-1]==side[j]:continue
                if side[j]+matchsticks[i]<=length:
                    side[j]+=matchsticks[i]
                    if bt(i+1):return True
                    side[j]-=matchsticks[i]
            return False
            
        return bt(0)
```
