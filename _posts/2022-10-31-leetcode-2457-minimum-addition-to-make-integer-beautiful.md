--- 
layout      : single
title       : LeetCode 2457. Minimum Addition to Make Integer Beautiful
tags        : LeetCode Medium Greedy Math Simulation
---
周賽317。前兩題做得很快，結果這邊腦袋打結噴三次WA，名次都掉光了。  

# 題目
輸入兩個正整數n和target。如果整數的數字之和小於等於target，則認為整數是**美麗的**。  
求最小的非負整數x使得n+x是**美麗的**。保證n一定可以變美麗。  

# 解法
比賽的時候把n轉成陣列來處理，沒有考慮到99+1=100這種情況。後來乾脆每次都重新統計數字總和，反正n最多10^12，那也只要統計12次而已。  

寫一個輔助函數f來計算數字總和，只要總和超過target則使最小的非0位元進位，將增加值加到答案中。重複步驟直到總和小於等於target為止。  

計算一次數字總和O(log n)，最差情況下要計算log n次，時間複雜度為O(log n * log n)。空間複雜度O(1)。  

```python
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        
        def f(n):
            return sum(int(x) for x in str(n))
        
        ans=0
        mul=1
        while f(n)>target:
            r=n%10
            if r>0:
                inc=10-r
                n+=inc
                ans+=inc*mul
            n//=10
            mul*=10
            
        return ans
```
