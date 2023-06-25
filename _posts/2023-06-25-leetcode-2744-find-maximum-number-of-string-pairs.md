--- 
layout      : single
title       : LeetCode 2744. Find Maximum Number of String Pairs
tags        : LeetCode Easy Array String Simulation HashTable
---
雙周賽107。這次周賽又被DDOS，大概卡了快一小時才恢復正常。  

# 題目
輸入由**不同**字串組成的陣列words。  

若滿足條件，words[i]可以和words[j]組成一對：  
- words[i]等於反轉後的words[j]  
- 0 <= i < j < words.length  

求words中**最多**可以組成幾對字串。  

注意：每個字串只能被配對一次。  

# 解法
題目保證words中每個字串都是獨一無二的，最多也只會有一種配對方式，不用考慮重複配對的狀況。  
直接窮舉所有組合(i,j)，如果滿足條件則答案+1。  

時間複雜度O(N^2)。  
空間複雜度O(1)。  

```python
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        N=len(words)
        ans=0
        
        for j in range(N):
            for i in range(j):
                if words[i]==words[j][::-1]:
                    ans+=1
                    break
                    
        return ans
```

既然知道每個字串只有一種配對可能，直接用雜湊表seen紀錄出現過的字串就好。  
遍歷字串w時檢查反轉過的w有沒有出現過，有的話答案+1；否則把w加到seen中。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen=set()
        ans=0
        
        for w in words:
            rev=w[::-1]
            if rev in seen:
                # seen.remove(rev)
                ans+=1
            else:
                seen.add(w)
                
        return ans
```