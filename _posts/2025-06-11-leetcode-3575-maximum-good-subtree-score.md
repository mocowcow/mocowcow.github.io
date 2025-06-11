---
layout      : single
title       : LeetCode 3575. Maximum Good Subtree Score
tags        : LeetCode Hard Tree DP BitManipulation Bitmask HashTable
---
biweekly contest 158。  
又是複雜度妙妙屋，這次妙到我想想都不敢寫。  
結果實際執行時間短到我傻眼，原來測資才 537 筆。算總時間真的每次都在賭會不會過。  

## 題目

<https://leetcode.com/problems/maximum-good-subtree-score/description/>

## 解法

每個數字只能出現一次，總共只有 10 種數字。  
不難想到 bitmask 狀態壓縮表示各數字是否出現。  

不同的選法可能出現相同的數字組合，有**重疊的子問題**，考慮 dp。  
定義 dp(i, mask)：以 i 為根的子樹中，出現狀態為 mask 的最大分數。  

---

對於每個節點 i 可能對應到 2^10 種 mask，但可能不會全出現，故以雜湊表 d[mask] 表示。  
不選擇任何節點對應到空集合 mask = 0，初始化空集合分數 d[0] = 0。  
然後檢查 vals[i] 是否存在重複。不重複則可用 vals[i] 產生對應的 mask。  

若 i 有子節點 j，則有若干個 dp(j, mask2)，以雜湊表 d2[mask2] 表示。  
考慮現有的 mask1 和子節點的 mask2 是否能有更好的組合。  
枚舉 mask1 和 mask2，若兩者無交集，則可以組成 new_mask = mask1 | mask2，其值為 d[mask] + d2[mask2]。  

最後將 d 所有選法中的最大分數加入答案。  

---

有 D = 10 種數字，共有 2^D 種 mask。  
枚舉兩種 mask 複雜度 O(2^D \* 2^D) = O(4^D)。  
光是這邊就高達 1e7，而且每個節點都要算，感覺就會超時。  

實際上每個節點只能提供一個 mask，至少需要合併 10 次才能達到 1024 種。  
每個子節點若要有 1024 種，也需要 10 次合併。  
而且還要濾掉有交集的部分，實際上是遠遠不及上限的。  

時間複雜度 O(N \* 4^D)，其中 D = 10。  
空間複雜度 O(N \* 2^D)。  

```python
MOD = 10 ** 9 + 7


class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        N = len(vals)
        g = [[] for _ in range(N)]
        for i in range(1, N):
            g[par[i]].append(i)

        @cache
        def dp(i):
            nonlocal ans
            d = Counter()
            d[0] = 0  # allow empty set
            val = vals[i]
            s = str(val)
            if len(s) == len(set(s)):
                mask = 0
                for x in s:
                    mask |= 1 << int(x)
                d[mask] = val

            for j in g[i]:
                d2 = d.copy()
                for mask, v1 in d.items():
                    for mask2, v2 in dp(j).items():
                        if mask & mask2 == 0:
                            new_mask = mask | mask2
                            d2[new_mask] = max(d2[new_mask], v1+v2)
                d = d2

            ans += max(d.values())
            return d

        ans = 0
        dp(0)

        return ans % MOD
```
