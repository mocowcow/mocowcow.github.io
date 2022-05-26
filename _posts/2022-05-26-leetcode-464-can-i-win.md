--- 
layout      : single
title       : LeetCode 464. Can I Win
tags        : LeetCode Medium DP Bitmask BitManipulation Math
---
隨便抽的一題，感覺最後的測資有點沒意思，故意放來卡人家WA的。  

# 題目
設計一個小遊戲，假設給定一個數字N，玩家可以選擇1\~N中任意一個數字，加到總和中，使總和超過目標值的人獲勝。每個數字只能被選用一次。  
輸入兩個整數maxChoosableInteger和desiredTotal，假設兩個玩家都發揮最佳，如果先手的玩家能贏，則回傳true，否則回傳false。  

# 解法
因為可選的數字N最大只到20，而且每個都只能用一次，很明顯可以用bitmask來表示每個數字的使用狀態。  

定義dp(mask,remain)：mask為當前可選擇的數字，而remain代表再加上多少數可以獲勝。  
玩家可以獲勝的情況有兩種：  
1. 當前某個可選的數字大於等於remain  
2. 選擇某個數之後後，使對手無法勝利  

所以遍歷每個可用的數字i，若當前數字大於等於remain，直接回傳true；否則將數字i標記為已使用，繼續遞迴下去。  
處理完所有可用數字後，若沒有符合的情況，代表無法勝利，只能回傳false。  

但是有一個很無聊的測資：  
> N=5, target=50  

1\~5全部加起來根本不到50，兩邊玩家根本都不可能贏，要在開頭加上檢查，避免出錯。

```python
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        N=maxChoosableInteger
        if N*(N+1)//2<desiredTotal:
            return False
        
        @cache
        def dp(mask,remain):
            for i in range(N):
                if not mask&(1<<i) and remain<=(i+1):
                    return True
                if not mask&(1<<i):
                    newMask=mask|(1<<i)
                    if not dp(newMask,remain-(i+1)):
                        return True
            return False
        
        return dp(0,desiredTotal)
```
