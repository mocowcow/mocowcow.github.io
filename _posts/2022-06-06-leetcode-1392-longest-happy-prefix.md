--- 
layout      : single
title       : LeetCode 1392. Longest Happy Prefix
tags        : LeetCode Hard String RollingHash
---
看到有人推薦的字串處理經典題，這種東西真的就是要靠經驗累積，應該沒什麼人能從0想出來。

# 題目
如果一個字串是一個**非空**前綴，同時也是後綴，那麼他就是一個**快樂前綴**。  
輸入字串s，回傳s的最長快樂前綴。若不存在則回傳空字串""。  

# 解法
最長的**前綴同時也是後綴**，相信一定有些同學覺得很耳熟。  
沒錯，就是KMP演算法所使用到的Longest Prefix also Suffix。  

KMP維護的partial match table，代表著字串s所有子字串的LPS長度，而table的最後一格就代表完整字串s的LPS。  
我們只要取s的LPS大小，並從s從頭切割子字串即可。  

```python
class Solution:
    def longestPrefix(self, s: str) -> str:
        def partial_match_table(s):  # PMT for KMP string search
            N = len(s)
            pmt = [0]*N
            i, j = 1, 0
            while i < N and j < N:
                if s[i] == s[j]:
                    j += 1
                    i += 1
                    pmt[i-1] = j
                elif j == 0:
                    i += 1
                else:
                    j = pmt[j-1]
            return pmt
        
        table=partial_match_table(s)
        mx=table[-1]
        return s[:mx]
```

另外一個方法是rolling hash，對所有前綴和後綴計算雜湊值。  
檢查相對的前後綴是否相等，若相等則以其長度更新mx。最後從s中切割出長度為mx的子字串。  

```python
class Solution:
    def longestPrefix(self, s: str) -> str:
        N=len(s)
        prefix=[0]*N
        suffix=[0]*N
        MOD=10**9+7
        h=0
        for i in range(N-1):
            c=ord(s[i])-97
            h=(h*26+c)%MOD
            prefix[i]=h
            
        h=0
        p=1
        for i in range(N-1,0,-1):
            c=ord(s[i])-97
            h=(h+c*p)%MOD
            suffix[i]=h
            p=(p*26)%MOD
        
        mx=0
        for i in range(N-1):
            if prefix[i]==suffix[N-i-1]:
                mx=i+1
                
        return s[:mx]
```