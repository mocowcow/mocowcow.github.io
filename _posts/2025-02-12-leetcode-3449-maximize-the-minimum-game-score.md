---
layout      : single
title       : LeetCode 3449. Maximize the Minimum Game Score
tags        : LeetCode Hard BinarySearch Greedy
---
weekly contest 436。

## 題目

<https://leetcode.com/problems/maximize-the-minimum-game-score/description/>

## 解法

看到**最小值最大化**就可以往**二分答案**去猜了。  
維護函數 ok(lim) 判斷是否能在 m 次操作使得每個位置都達到 lim。  

但難點在於如何實現判斷函數。  
根據經驗，二分答案的判斷函數通常都是 O(N)，只需要遍歷陣列一次。  

---

從左邊出發，試著使得每個索引都滿足 lim。  
對於索引 i 來說，至少需要 need = ceil(points[i] / lim) 次操作。  
而從 i-1 移動到 i 就保底一次操作，還需要 need-1 次。  

但每次操作前都需要先移動，沒辦法連續操作同一個索引，因此需要先跳到 i+1 再跳回來。  
扣掉**i-1 到 i 的一次操作**，還需要**先到 i+1 再回 i** 重複 need-1 次。  
所以滿足索引 i 共需操作次數：  
> (need-1) \* 2 + 1  
> = need \* 2 - 1  

---

剛才提到了**先跳到 i+1**，那這些次數可不能浪費。  

對於 i 來說，如果有來回跳，則 i+1 就可以減少相同操作次數。  
維護變數 pre，代表對於當前 i 來說，經由 i-1 已經操作的次數。  
初始值為 0，並每次更新成 need-1。  
i 的操作次數需要更改成 need = ceil(points[i] / lim) - pre。  

---

但又有個問題：如果扣掉 pre 之後，need 變 0 或是負數怎麼辦？  

- i < N-1，右邊還有索引需要處理。  
    當前 i 沒有來回跳，所以 i+1 肯定沒操作過。  
    所以還需要去 i+1，改 need = 1。  
- i == N-1，已經是最後一個索引。  
    操作結束。  

---

按照上述方法實現 ok(lim)，並套用二分。  
最差情況下 m = 0，每個索引都只能是 0，下界 = 0；  
最好情況下 N = 2，兩個索引平分 m 次，上界 = max(points) * m。  

時間複雜度 O(N log MX)，其中 MX = min(points) \* m。  
空間複雜度 O(1)。  

```python
class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        N = len(points)

        def ok(lim):
            cnt = 0
            pre = 0
            for i, x in enumerate(points):
                need = (lim + x - 1) // x
                need -= pre

                if need < 1:
                    if i < N - 1:
                        need = 1
                    else: # i == N - 1
                        break # fininshed
                
                # i-1 to i "one times"
                # and i to i+1 for "need-1 times"
                # and i+1 to i for "need-1 times"
                # therefore, i got "need" times 
                # and i+1 got "need-1" times
                cnt += need * 2 - 1
                pre = need - 1
            return cnt <= m

        lo = 0
        hi = max(points) * m
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if not ok(mid):
                hi = mid - 1
            else:
                lo = mid

        return lo
```
