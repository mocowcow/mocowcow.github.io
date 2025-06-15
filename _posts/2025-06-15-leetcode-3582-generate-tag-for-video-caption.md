---
layout      : single
title       : LeetCode 3582. Generate Tag for Video Caption
tags        : LeetCode Easy Simulation
---
weekly contest 454。

## 題目

<https://leetcode.com/problems/generate-tag-for-video-caption/description/>

## 解法

暴力模擬。  
第一個詞改全小寫，其他詞開頭大寫。  
最後加上 "#" 後保留 100 長度。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def generateTag(self, caption: str) -> str:
        a = caption.split()
        for i, w in enumerate(a):
            if i == 0:
                a[0] = w.lower()
            else:
                a[i] = w[0].upper() + w[1:].lower()

        ans = "#" + "".join(a)
        return ans[:100]
```
