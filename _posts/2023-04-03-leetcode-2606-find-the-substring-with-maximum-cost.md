--- 
layout      : single
title       : LeetCode 2606. Find the Substring With Maximum Cost
tags        : LeetCode Medium Array Greedy DP HashTable
---
雙周賽101。這題目包裝得很棒，懂的人就知道是kadane。  

# 題目
輸入字串s，以及由**不同字元**組成的字串chars，還有整數陣列vals。chars和vals長度相同。  

一個**子字串的成本**為其所有字元的價值總和。空字串成本為0。  

每個**字元的價值**定義如下：  
- 如果該字元不在chars中，則其價值為在字母中的順序。例如a為1、b為2  
- 否則，該字元為char[i]，則價值為vals[i]  

求子字串的**最大成本**為多少。  

# 解法
非常經典的kadaen maximum subarray。  

首先維護雜湊表mp，把chars中字元所對應的價值紀錄。  
遍歷s中每個字元c作為子陣列的結尾，如果前一次的結果小於0就丟掉，直接開始新的子陣列；否則繼續接上。  
如果c在mp中就加上mp[c]；否則以ascii算出其價值。  

注意：題目允許空字串，所以答案初始值為0。  

時間複雜度O(M+N)，其中M為chars長度，N為s長度。空間複雜度O(M)。  

```python
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        mp={c:v for c,v in zip(chars,vals)}
        curr=0
        ans=0
        
        for c in s:
            if c in mp:
                curr=max(curr,0)+mp[c]
            else:
                curr=max(curr,0)+ord(c)-97+1
            ans=max(ans,curr)
        
        return ans
```

或是一開始就先把ascii順序寫好，再以chars對應的價值更新雜湊表，這樣子就不必特例檢查了。  

```python
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        mp={chr(97+i):i+1 for i in range(26)}
        mp2={c:v for c,v in zip(chars,vals)}
        mp.update(mp2)
        curr=0
        ans=0
        
        for c in s:
            curr=max(curr,0)+mp[c]
            ans=max(ans,curr)
        
        return ans
```