---
layout      : single
title       : LeetCode 3043. Find the Length of the Longest Common Prefix
tags        : LeetCode Medium Array String Simulation
---
周賽385。直接上字典樹模板。省了打字時間，結果有地方沒改好，拿一隻蟲，虧死。  

## 題目

輸入正整數陣列 arr1 和 arr2。  

正整數的**前綴**是由**最靠左**的一或多個數字組成。例如 123 是 12345 的前綴，但 234 不是。  

若存在一個整數 c，同時是整數 a 和 b 的前綴，則稱 c 為**公共前綴**。例如 5655359 和 56554 有公共前綴 565，而 1223 和 43456 沒有公共前綴。  

你必須找到所有整數對 (x, y) 之中的**最長公共前綴**的長度，其中 x 屬於 arr1，而 y 屬於 arr2。  

回傳所有數對中的**最長**公共前綴長度。若不存在則回傳 0。  

## 解法

最暴力的方法，直接把每個數都轉成字串，然後枚舉前綴。  
先把 arr1 的前綴加入集合，然後枚舉 arr2 的前綴，若有出現過則以當前前綴長度更新答案。  

數字上限 MX = max(arr[i]) = 10^8，轉成字串也就 8 個字元。  
數字轉字串需要 O(log MX)。然後有 O(log MX) 個前綴，每次字串切片也要 O(log MX)。  

時間複雜度 O((M+N) \* log MX \* log MX)，其中 M 為 arr1 長度，N 為 arr2 長度。  
空間複雜度 O(M \* log MX \* log MX)。  

```python
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        pref = set()
        for x in arr1:
            s = str(x)
            for i in range(len(s)):
                pref.add(s[:i+1])
                    
        ans = 0
        for x in arr2:
            s = str(x)
            for i in range(len(s)):
                if s[:i+1] in pref:
                    ans = max(ans, i+1)
                    
        return ans
```
