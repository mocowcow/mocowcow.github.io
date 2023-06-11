--- 
layout      : single
title       : LeetCode 2730. Find the Longest Semi-Repetitive Substring
tags        : LeetCode Medium String Simulation TwoPointers
---
雙周賽106。

# 題目
輸入由數字0\~9組成的字串s。  

如果一個字串t中最多只有一組相鄰且相同的數字，則稱為**半重複**。例如0010, 002020, 0123, 2002, 和54944都是半重複；而00101022和1101234883不是。  

求s最長的**半重複**子字串長度。  

# 解法
測資很小，一樣靠暴力解決。  
窮舉所有子字串，枚舉所有相鄰數對，若重複不超過一組則以子字串長度更新答案。  

時間複雜度O(N^3)。  
時間複雜度O(N)。  

```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        N=len(s)
        
        def ok(sub):
            rep=0
            for a,b in pairwise(sub):
                if a==b:
                    rep+=1
            return rep<2
        
        ans=1
        for i in range(N):
            for j in range(i,N):
                sub=s[i:j+1]
                if ok(sub):
                    ans=max(ans,j-i+1)
                    
        return ans
```

假設一個索引對(i,j)是重複的，之後又出現另一個重複的索引對(k,l)，所以子字串s[i,l]中有兩次重複，所以不合法；但是s[j+1,l]就只剩下一次重複，完全合法。  

只要記錄上一次出現重複的後面那個索引(也就是j)，在找到下一個重複的時候更新子陣列左邊界為j，就可以得到合法的範圍。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        N=len(s)
        ans=1
        j=0
        left=0
        
        for right in range(1,N):
            if s[right]==s[right-1]:
                left=j
                j=right
            ans=max(ans,right-left+1)
            
        return ans
```