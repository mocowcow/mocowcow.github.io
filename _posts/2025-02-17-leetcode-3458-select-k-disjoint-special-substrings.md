---
layout      : single
title       : LeetCode 3458. Select K Disjoint Special Substrings
tags        : LeetCode Medium Greedy Sorting
---
weekly contest 437。

## 題目

<https://leetcode.com/problems/select-k-disjoint-special-substrings/description/>

## 解法

**特殊子字串**指的是相同字元都必須包含在子字串內。  
對於每個字元，都需要知道**第一次**和**最後一次**出現的位置，這也是包含該字元的最小區間範圍。  

在每個字元都不互相交錯時，至多 26 個不重疊區間。  

---

但有時後字元會互相交錯。例如：  
> s = "aabb"  
> s = "abab"  

前者可以單獨選擇 "aa" 或 "bb"；當然也可以一起選 "aabb"，但沒意義。  
後者只能一起選 "abab"。  

為了得知真正的區間，需要維護當前子字串邊界 [lb, rb]，並從中間往左右擴展，以碰到的字元不斷更新邊界。  
最差情況下也只會遍歷者整個字串，時間複雜度 O(N \* MX)。  

注意：子字串不可與整個 s 相同，需要特判。  

---

求出所有區間後，問題轉換成求**不重疊區間數**。  
相似題 [435. non overlapping intervals]({% post_url 2023-07-19-leetcode-435-non-overlapping-intervals %})。  

判斷是否存在至少 k 個不重疊區間，時間複雜度為排序 O(MX log MX)。  

時間複雜度 O(N \* MX + MX log MX)，其中 MX = 不同字元個數。  
空間複雜度 O(MX)。  

```python
class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        N = len(s)
        first = {}
        last = {}
        for i, c1 in enumerate(s):
            if c1 not in first:
                first[c1] = i
            last[c1] = i

        a = []
        for c1, lb in first.items():
            rb = last[c1]
            i = j = lb
            while lb <= i or j <= rb:
                while lb <= i:
                    c2 = s[i]
                    lb = min(lb, first[c2])
                    rb = max(rb, last[c2])
                    i -= 1
                while j <= rb:
                    c2 = s[j]
                    lb = min(lb, first[c2])
                    rb = max(rb, last[c2])
                    j += 1

            if lb != 0 or rb != N-1:
                a.append([lb, rb])

        # non-overlapping intervals
        a.sort(key=itemgetter(1))
        ans = 0
        pre = -inf
        for s, e in a:
            if pre < s:
                ans += 1
                pre = e

        return ans >= k
```
