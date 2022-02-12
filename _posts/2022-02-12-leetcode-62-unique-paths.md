---
layout      : single
title       : LeetCode 62. Unique Paths
tags 		: LeetCode Medium DP
---
DP教學系列。這種算路徑的都比較直觀，可以輕鬆的找出bottom-up解。

# 題目
輸入一個M*N矩陣。從左上角出發，每次移動只能往右或是往下走，求走到右下角有多少種路線。

# 解法

>步驟1：定義狀態  

影響的變數有x,y軸，需要二維DP。  
dp[r][c]代表在(r,c)到達位置路線數。

>步驟2：找出狀態轉移方程式  

只能往右或下走，換個說法就是每個位置只能由上方或是左方過來。  
到達(r,c)的路線=到達上方路線+到達左方路線，dp[r][c]=dp[r-1][c]+dp[r][c-1]。

>步驟3：處理base cases

如果在r=0或是c=0的時候，只有一個來源，在起點(0,0)時甚至沒有來源，所以r或c=0的點全部設為1。

自上而下，自左而右，r,c都從1開始處理，就不用管base cases。直接更新元素也不影響結果，空間可以壓縮到一維。

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n

        for _ in range(1, m):
            for i in range(1, n):
                dp[i] += dp[i-1]

        return dp[-1]
```
