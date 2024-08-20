---
layout      : single
title       : LeetCode 3258. Count Substrings That Satisfy K-Constraint I
tags        : LeetCode Easy String SlidingWindow TwoPointers
---
weekly contest 411。  

## 題目

輸入**二進位**字串 s，以及整數 k。  

若一個二進位字串滿足以下**任一**條件，則稱其 **k 約束**。  

- 字串中最多 k 個 0。  
- 字串中最多 k 個 1。  

求 s 有幾個 **k 約束** 子字串。  

## 解法

暴力枚舉所有子字串，並統計 0,1 個數。  

時間複雜度 O(N^3)。  
空間複雜度 O(N)。  

```python
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        N = len(s)
        ans = 0
        for i in range(N):
            for j in range(i, N):
                sub = s[i:j+1]
                cnt0 = sub.count("0")
                cnt1 = sub.count("1")
                if min(cnt0, cnt1) <= k:
                    ans += 1

        return ans
```

當我們枚舉固定長度的子字串時，每次只會加入一個新的、刪去一個舊的。  
因此枚舉窗口大小 sz，並搭配**滑動窗口**維護 0,1 的個數。  

時間複雜度 O(N^2)。  
空間複雜度 O(1)。  

```python
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        N = len(s)
        ans = 0
        for sz in range(1, N+1):
            left = cnt1 = cnt0 = 0
            for right, x in enumerate(s):
                # expand right bound
                if x == "1":
                    cnt1 += 1
                else:
                    cnt0 += 1

                if right - left + 1 == sz:
                    if min(cnt0, cnt1) <= k:
                        ans += 1
                    # shrink left bound
                    if s[left] == "1":
                        cnt1 -= 1 
                    else:
                        cnt0 -= 1
                    left += 1

        return ans
```

若某字串是 **k 約束**的，其子字串肯定也是。  
其實只需要枚舉索引作為右端點 right，並找出其最遠的左端點 left。  
對於 right 來說，區間 [left, right] 都可以作為合法的左端點，因此對答案貢獻 right - left + 1 個。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        left = cnt1 = cnt0 = 0
        for right, x in enumerate(s):
            # expand right bound
            if x == "1":
                cnt1 += 1
            else:
                cnt0 += 1

            # shrink left bound
            while min(cnt0, cnt1) > k:
                if s[left] == "1":
                    cnt1 -= 1 
                else:
                    cnt0 -= 1
                left += 1
            ans += right - left + 1

        return ans
```
