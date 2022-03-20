---
layout      : single
title       : LeetCode 2209. Minimum White Tiles After Covering With Carpets
ㄒtags 		: LeetCode Hard String DP
---
雙周賽74。看第一眼就知道是DP，可是腦子沒轉過來，一直想著怎麼保存修改後的字串，到最後都沒想出DP定義。

# 題目
字串floor由"0"和"1"組成，分別代表黑色和白色的磁磚。你有numCarpets條黑色的地毯，長度都是carpetLen。  
試著用地毯盡可能將白色磁磚覆蓋住，求白色磁磚的露出數最多能降低到多少。地毯可以互相重疊。

# 解法
比賽結束後看了人家定義馬上就寫出來了，以第四題來說難度算是相當低了，好可惜。  

dp(i,k)表示到floor[i]為止，剩下k條地毯，最少有幾片白色磁磚。  
每次可以選擇蓋或不蓋，轉移方程式為：dp(i,k)=min(不蓋,蓋)。  
若不蓋，磁磚數等於dp(前一格，毛毯數不變)，若當前floor[i]為白色，則多+1；若要蓋，則等於dp(當前格-毛毯長度, 毛毯數-1)。  
edge cases：磁磚起點為0，i<0沒有任何磁磚，回傳0。地毯也不可以多用，k<0時代表沒地毯了，回傳inf代表不可能達成。

```python
class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        N=len(floor)
        if numCarpets*carpetLen>=N:
            return 0
        
        @lru_cache(None) 
        def dp(i,k):
            if k<0:
                return math.inf
            if i<0:
                return 0
            skip=dp(i-1,k)+(floor[i]=='1')
            cover=dp(i-carpetLen,k-1)
            return min(skip,cover)
            
        return dp(N-1,numCarpets)
```

