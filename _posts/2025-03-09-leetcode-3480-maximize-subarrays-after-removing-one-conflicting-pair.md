---
layout      : single
title       : LeetCode 3480. Maximize Subarrays After Removing One Conflicting Pair
tags        : LeetCode Hard
---
weekly contest 440。  

## 題目

<https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/solutions/6515832/python-greedy/>

## 解法

求 [1..n] 有多少子陣列，不包含任意衝突對 (a,b)。  
求子陣列問題，通常會利用**滑動窗口**，或是枚舉左端點 (或右端點)、維護另一個端點，求出數量。  

---

先不考慮衝突對，若子陣列以 i 為左端點，其右端點可以是 [i..n]。  

再考慮衝突對 (a,b)，保證 a < b。  
子陣列不可同時包含 a 和 b，所以只有滿足 i <= a 的衝突對才會影響到以 i 為左端點的子陣列 (若 a < i 則永遠不可能包含 a)。  
加入衝突對 (a,b) 後，i 的右端點可用區間變為 [i..b-1]。  
共 b - i 個子陣列。  

考慮多個衝突對 (a1,b2), (a2,b2), ..., (ai,bi)，且都滿足 i <= a。  
因為保證 a < b，所以只要避免取到任意一個 b。右端點可用區間變為 [i..min(b)-1]。  
共 min(b) - i 個子陣列。  

先以 a 為鍵值將衝突對分組，從 n 到 1 枚舉左端點 i，以滿足 i = a 的衝突對 (a,b) 更新 b 的最小值。  

---

接下來考慮刪除哪一個衝突對。  

剛才說了不考慮不在乎 a 只在乎 b。  
現在有 b1, b2, ..., bi，滿足 b1 <= b2 <= ... <= bi。  
如果刪了 b1 之外的對，右端點依然受限於 b1；只有刪了 b1，才能使右端點改受限於 b2。  

只有在 b1 < b2 時，刪除 (a1,b1)，使右端點從 b1 - 1 擴張成 b2 - 1，**增加 b2 - b1 個子陣列**。  
我們只需要維護**最小的兩個** b，即 b1, b2。  

---

現在我們知道，對於每個左端點 i 來說，只有唯一的刪除選擇，即刪除 b1 所屬的衝突對。  

先將使衝突對滿足 a < b ，給定編號 pid。  
從 n 到 1 枚舉左端點 i，至少有 b1 - i 個子陣列，加入 ans。  
若 b1 < b2，刪除 b1 所屬的衝突對 pairs[pid1] 會新增 b2 - b1 個子陣列，加到 extra[pid1] 裡面。  

答案即 ans + max(extra)。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        M = len(conflictingPairs)
        pairs = [[] for _ in range(n+1)]
        for pid, (a, b) in enumerate(conflictingPairs):
            if a > b:
                a, b = b, a
            pairs[a].append([b, pid])

        ans = 0
        extra = [0] * (M+1)
        # maintan 2 smallest (_, b)
        b1 = b2 = n+1 # [1..n+1) = [1..n]
        pid1 = pid2 = -1
        for i in reversed(range(1, n+1)):
            for b, pid in pairs[i]:
                if b < b1:
                    b1, b2 = b, b1
                    pid1, pid2 = pid, pid2
                elif b < b2:
                    b2 = b
                    pid2 = pid

            # subarrays without removal
            ans += b1 - i
            # extra subarrays if remove pairs[pid1] = (_, b1)
            if b1 < b2:
                extra[pid1] += b2 - b1

        return ans + max(extra)
```

仔細想想，若存在 (a1,b1), (a2,b2) 滿足 b1 == b2 會怎樣？  
例如：  
> pairs = (3,7), (5,7)  
> i = 3  
> b1 = 7, b2 = 7  

不管刪除哪對，都不可能使得右端點變更遠。  
對於更小的 i 來說，同樣也無法受益於刪除；就算出現了更小的衝突對，例如 (2, 6)，也只會刪除 (2, 6) 而已。  

發現只要同有兩個以上的衝突對共享相同 b 值，只有 a 最大的那對有機會被刪除，也就是從右向左遍歷時碰到的第一個碰到的 (_, b) 衝突對。  
因此可以直接**拿 b 當作刪除的衝突對的編號**。  

```python
class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        pairs = [[] for _ in range(n+1)]
        for a, b in conflictingPairs:
            if a > b:
                a, b = b, a
            pairs[a].append(b)

        ans = 0
        extra = [0] * (n+2)
        b1 = b2 = n+1 # maintan 2 smallest (_, b)
        for i in reversed(range(1, n+1)):
            for b in pairs[i]:
                if b < b1:
                    b1, b2 = b, b1
                elif b < b2:
                    b2 = b

            # subarrays without removal
            ans += b1 - i
            # extra subarrays if remove (_, b1)
            extra[b1] += b2 - b1

        return ans + max(extra)
```
