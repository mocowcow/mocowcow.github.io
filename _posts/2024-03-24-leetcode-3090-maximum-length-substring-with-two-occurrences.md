---
layout      : single
title       : LeetCode 3090. Maximum Length Substring With Two Occurrences
tags        : LeetCode Easy Array HashTable TwoPointers SlidingWindow
---
周賽 390。

## 題目

輸入字串 s，求 s 的最長子字串，其中每個字元最多出現兩次。  

## 解法

暴力法。枚舉所有子字串並檢查，若滿足條件則更新答案。  

時間複雜度 O(N^3)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        N = len(s)
        
        def ok(sub):
            d = Counter(sub)
            for v in d.values():
                if v > 2:
                    return False
            return True
        
        ans = 0
        for i in range(N):
            for j in range(i, N):
                sub = s[i:j + 1]
                if ok(sub):
                    ans = max(ans, len(sub))
                    
        return ans
```

更好的方法是**滑動窗口**。  
相似題 [3. longest substring without repeating characters]({% post_url 2022-06-10-leetcode-3-longest-substring-without-repeating-characters %})。  

時間複雜度 O(N)。  
空間複雜度 O(26)。  

```python
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        d = Counter()
        left = 0
        for right, c in enumerate(s):
            d[c] += 1
            while d[c] >2:
                d[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
            
        return ans
```
