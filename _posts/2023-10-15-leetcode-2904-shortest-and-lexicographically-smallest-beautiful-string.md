---
layout      : single
title       : LeetCode 2904. Shortest and Lexicographically Smallest Beautiful String
tags        : LeetCode Medium String Simulation SlidingWindow TwoPointers
---
周賽367。

## 題目

輸入二進位字串s，還有正整數k。  

如果一個s的子字串正好包含k個1字元，則稱為**美麗的**。  

令len為**最短**美麗子字串的長度。  

回傳字典序**最小**、且長度為len的美麗子字串。若不存在則回傳空字串。  

## 解法

從小到大枚舉子字串長度size，並維護長度為size的最小美麗子陣列。若找到直接回傳。  

時間複雜度O(n^3)。  
空間複雜度O(n)。  

```python
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        N=len(s)
        ans=""
        
        for size in range(1,N+1):
            for i in range(N):
                sub=s[i:i+size]
                if sub.count("1")==k and (ans=="" or sub<ans):
                    ans=sub
            if ans!="":
                return ans
                    
        return ""
                    
```

也可以枚舉子字串左起點i，擴展右邊界j，並計算字元1的個數。  
找滿k個則以當前子字串s[i,j]更新答案。  

要使得子字串盡可能小，所以不可能有前導零，若nums[i]可以直接跳過不處理。  

時間複雜度O(N^2)。  
空間複雜度O(N)。  

```python
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        N=len(s)
        ans=""
        
        for i in range(N):
            if s[i]!="1":
                continue
            cnt=0
            for j in range(i,N):
                if s[j]=="1":
                    cnt+=1
                if cnt==k:
                    sub=s[i:j+1]
                    if ans=="" or \
                    len(sub)<len(ans) or \
                    (len(sub)==len(ans) and sub<ans):
                        ans=sub
                    break
                    
        return ans
```

另一種思路是滑動窗口：維護一個擁有k個1的窗口，並以當前窗口做為子字串更新答案。  

雖然均攤下來，每個s[i]最多被處理兩次，但是更新答案時需要構造子字串，每次時間還是O(N)。  
時間複雜度O(N^2)。  
空間複雜度O(N)。  

```python
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        N=len(s)
        ans=""
        i=0
        cnt=0
        
        for j,c in enumerate(s):
            if c=="1":
                cnt+=1
            while cnt==k:
                sub=s[i:j+1]
                if ans=="" or len(sub)<len(ans) or (len(sub)==len(ans) and sub<ans):
                    ans=sub
                if s[i]=="1":
                    cnt-=1
                i+=1
            
        return ans
```
