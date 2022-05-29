--- 
layout      : single
title       : LeetCode 318. Maximum Product of Word Lengths
tags        : LeetCode Medium String Array HashTable Bitmask BitManipulation
---
每日題。其實用set就能過，不知道為什麼沒有對應的標籤。

# 題目
輸入字串陣列words，回傳length(word[i]) * length(word[j])的最大值，且兩個單字沒有使用共同的字母。  
如果不存在符合條件的兩個單字，則回傳0。

# 解法
以前第一次做的時候還不懂bitmask，就選用set來做。  
先把每個單字w裝進set，並記錄其長度。  
之後兩兩遍歷所有單字的set，檢查其有無交集，若無則以兩者長度相乘更新答案。

```python
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        N = len(words)
        words = [(set(w), len(w)) for w in words]
        ans = 0
        for i in range(N):
            for j in range(i+1, len(words)-):
                if words[i][0].isdisjoint(words[j][0]):
                    ans = max(ans, words[i][1]*words[j][1])

        return ans
```

但天看到題目的第一反應竟然就是bitmask，看來bitmask已經是我的好朋友了。  

先寫一個輔助函數getMask(w)，傳入單字，將其轉換成bitmask。  
維護雜湊表masks，紀錄各mask對應的最大長度。  
遍歷words中每個單字，先求出其對應的mask及長度，並對先前已經出現過的所有mask做比對，若無交集則以兩者長度更新答案。最後記得將當前的mask加回到masks中。

```python
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        def getMask(w):
            mask=0
            for c in w:
                mask|=(1<<(ord(c)-97))
            return mask
        
        N=len(words)
        masks=defaultdict(int)
        ans=0
        for i in range(N):
            m1=getMask(words[i])
            size=len(words[i])
            for m2 in masks:
                if m1&m2==0:
                    ans=max(ans,size*masks[m2])
            masks[m1]=max(masks[m1],size)

        return ans
```