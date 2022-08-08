--- 
layout      : single
title       : LeetCode 2370. Longest Ideal Subsequence
tags        : LeetCode Medium Array DP
---
周賽305。第一次看到Q4是medium，但我卻一點頭緒都沒有。賽後才知道這題也是DP，當下心情真的糟到一個不行。  
難得Q3和Q4都是理應擅長的DP，結果兩題都沒發現，真的該好好反省。  

# 題目
輸入由小寫字母組成的字串s，以及整數k。若滿足以下條件，我們稱字串t是**理想的**：  
- t是s的子序列  
- 對於t兩兩相鄰的字母，其字典順序的**絕對差**小於等於k  

求最長的**理想子序列**長度為何。

注意，字母順序不是循環的。例如"a"和"z"的順序絕對差為25，而非1。  

# 解法
其實有點類似LIS的概念，差別在於LIS是找前方**結尾元素小於當前元素的子序列**中**長度最大者**；而本題是找前方**結尾元素與當前元素字典絕對差不超過k者**中**長度最大者**。  

建立長度為26的dp陣列，分別代表a\~z結尾的子序列長度。  
遍歷nums中每個字元c，並列舉26個字母，若兩者字典差小於等於k，則更新最大長度best。最後以best+1更新以c結尾的子序列長度。  
處理完整個s字串後，dp陣列中最大者就是答案。  

```python
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp=[0]*26
        
        for c in s:
            i=ord(c)-97
            best=0
            for j in range(26):
                if abs(i-j)<=k:
                    best=max(best,dp[j])
            dp[i]=best+1
            
        return max(dp)
```
