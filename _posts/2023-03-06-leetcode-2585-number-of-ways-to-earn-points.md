--- 
layout      : single
title       : LeetCode 2585. Number of Ways to Earn Points
tags        : LeetCode Hard Array DP
---
周賽335。第二次在同一周內AK雙周賽+周賽，好開心。  

# 題目
某場考試中，共有n種類的題型。輸入整數target和二維整數陣列types，其中types[i] = [count<sub>i</sub>, marks<sub>i</sub>]代表第i種題型有count<sub>i</sub>題，答對每題可以獲得marks<sub>i</sub>分。  

求總共有多少方式可以達到**正好**target分。答案很大，先模10^9+7後回傳。  

注意：同類型的題目無法被區分：  
- 例如某題型有3題，答對第1,2題或是答對第2,3題被視為相同的方式  

# 解法
多重背包問題，和一般的01背包差別在於一種東西有好幾個。  

定義dp(i,sm)：考慮第i個題型時，且當前分數為sm時，能夠達到target分的方案。  
轉移方程式：令types[i] = cnt, mark，當前題型有cnt題，每題提供mark分，可以選擇作答本題0\~cnt次。  
即dp(i,sm) = sum(dp(i+1,sm+mark\*j)) FOR ALL 0 <= j <= cnt  
base cases：當sm正好為target，得到1種方案；sm超過target不合法，0種方案；i等於N時且sm不為target，沒有剩下的題目了，0種方案。  

時間複雜度O(target \* N \* max(count))，其中N為types長度。空間複雜度O(target \* N)。  

```python
class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD=10**9+7
        N=len(types)
        
        @cache
        def dp(i,sm):
            if sm==target:return 1
            if i==N:return 0
            if sm>target:return 0
            ans=0
            cnt,mark=types[i]
            for j in range(cnt+1):
                ans=(ans+dp(i+1,sm+mark*j))%MOD
            return ans
        
        return dp(0,0)
```