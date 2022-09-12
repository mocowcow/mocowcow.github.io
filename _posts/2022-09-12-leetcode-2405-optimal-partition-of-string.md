--- 
layout      : single
title       : LeetCode 2405. Optimal Partition of String
tags        : LeetCode Medium String Greedy HashTable Bitmask BitManipulation
---
周賽310。這題其實直覺秒殺，比Q1還簡單。  

# 題目
輸入字串s，將該字串劃分為一個或多個子字串，使得每個子符串中每個字元最多出現1次。  
求最少需要幾個子字串。  

注意，每個字元都要被分到某個子字串中。  

# 解法
子字串一定是連續的，那我們只要依序記錄那些字元已經出現過就好。  

s長度至少1，代表子字串最少要有一個，ans初始化為1。  
遍歷每個字元c，若c已經出現過則建立新的子字串，ans+1，並把集合清空。最後將c加入集合，表示已經出現過。  
時間複雜度O(N)，而字元只會出現a\~z，實際上是常數，空間複雜度O(1)。  

```python
class Solution:
    def partitionString(self, s: str) -> int:
        seen=set()
        ans=1
        
        for c in s:
            if c in seen:
                seen=set()
                ans+=1
            seen.add(c)
        
        return ans
                
```

也可以用bitmask來表示各字母的出現狀態，雖然執行起來反而變慢。  

```python
class Solution:
    def partitionString(self, s: str) -> int:
        ans=1
        mask=0
        
        for c in s:
            i=ord(c)-97
            if mask&(1<<i):
                mask=0
                ans+=1
            mask|=(1<<i)
            
        return ans
```                
