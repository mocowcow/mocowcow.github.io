--- 
layout      : single
title       : LeetCode 2696. Minimum String Length After Removing Substrings
tags        : LeetCode Easy String Simulation
---
周賽346。

# 題目
輸入由大寫字母組成的字串s。  

你可以從s中刪除子字串"AB或是"CD"任意次。  

求經過數次刪除後，s的最短長度為多少。  

注意，刪除一個子字串後有可能產生新的"AB或是"CD"。  

# 解法
直接暴力查找，如果AB或CD有在s中就取代成空字串。  
每次查找、取代都是O(N)。  

最差情況下查找N次，時間複雜度O(N^2)。  
空間複雜度O(1)。  

```python
class Solution:
    def minLength(self, s: str) -> int:
        while "AB" in s or "CD" in s:
            s=s.replace("AB","")
            s=s.replace("CD","")
            
        return len(s)
```
