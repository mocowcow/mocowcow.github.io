---
layout      : single
title       : LeetCode 2914. Minimum Number of Changes to Make Binary String Beautiful
tags        : LeetCode Medium String Greedy
---
雙周賽116。

## 題目

輸入偶數長度的二進位字串s。  

如果s可以分割成1或多個滿足以下條件的子字串，則稱為**美麗的**。  

- 每個子字串都是偶數長度  
- 每個子字串只包含1，或是只包含0  

你可以將s中的任何字元修改成0或是1。  

求使得s成為美麗的字串所需的**最小修改次數**。  

## 解法

雖然說可以分割，但分割成多少個子字串並不是重點。  
例如1111可以維持1111，或是分割成11+11，兩者都是美麗的。  

既然如此，乾脆把s看做好幾個長度2的子字串組成，只要確保每個子字串都是11或是00即可。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def minChanges(self, s: str) -> int:
        N=len(s)
        ans=0
        
        for i in range(0,N,2):
            if s[i]!=s[i+1]:
                ans+=1
                
        return ans
```
