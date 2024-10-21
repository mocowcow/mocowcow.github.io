---
layout      : single
title       : LeetCode 3325. Count Substrings With K-Frequency Characters I
tags        : LeetCode Medium SlidingWindow TwoPointers
---
weekly contest 420。  
這陣子常常出這種滑窗模板題。  
說起來這次竟然只有基本款 I，或許過幾天就放強化版 II。  

## 題目

輸入字串 s 和整數 k。  
求 s 有多少**子字串**中，**至少**有一個字元**至少**出現 k 次。  

## 解法

子字串問題就會想到滑窗。  
相似題 [3297. count substrings that can be rearranged to contain a string i.md]({% post_url 2024-09-22-leetcode-3297-count-substrings-that-can-be-rearranged-to-contain-a-string-i %})。  

只要窗口中最大的出現頻率大於等於 k 就合法。  
對於每個右端點 right，只要合法就不斷收縮左端點 left。  
區間 [0, left-1] 內的所有數都可以與 right 組成合法的子字串。  

時間複雜度 O(26N)。  
空間複雜度 O(26)。  

```python
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        ans = 0
        d = Counter()
        left = 0
        for right, c in enumerate(s):
            d[c] += 1
            while max(d.values()) >= k:
                d[s[left]] -= 1
                left += 1
            # [0, left-1] 
            # ans += left - 1 - 0 + 1
            ans += left

        return ans
```

注意到每次擴展右端點時，只有 s[right] 的頻率會增加，也只有 s[right] 有可能出現 k 次。  
因此只需以 s[right] 頻率作為合法的判斷標準。  

時間複雜度 O(N)。  
空間複雜度 O(26)。

```python
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        N = len(s)
        ans = 0
        d = Counter()
        left = 0
        for right, c in enumerate(s):
            d[c] += 1
            while d[c] >= k:
                d[s[left]] -= 1
                left += 1
            # [0, left-1] 
            # ans += left - 1 - 0 + 1
            ans += left

        return ans
```
