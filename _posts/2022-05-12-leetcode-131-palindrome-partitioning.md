--- 
layout      : single
title       : LeetCode 131. Palindrome Partitioning
tags        : LeetCode Medium Array Backtracking 
---
複習回溯的經典題。

# 題目
輸入字串s，試著將s分成多個**回文子字串**，求所有的分組可能。  
回文指的是向後讀取與向前讀取結果相同的字串。

# 解法
檢查回文最簡單的方式，就是將字串反轉後檢查是否相同。  
使用回溯法，從起點i列舉每個可能的子字串，若子字串符合回文，則將其加入curr，繼續分割下一段，重複至所有字元用完為止。

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N=len(s)
        ans=[]
        
        def bt(i,curr):
            if i==N:
                ans.append(curr[:])
            else:
                for j in range(i,N):
                    sub=s[i:j+1]
                    if sub==sub[::-1]:
                        curr.append(sub)
                        bt(j+1,curr)
                        curr.pop()
                
        bt(0,[])
        
        return ans
```

上面的方法需要產生好幾次子字串，而且檢查回文的方式沒效率。  
可以用雙指標的方法，直接在s裡面檢查回文。

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N=len(s)
        ans=[]
        
        def isPalindrome(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l,r=l+1,r-1
            return True
            
        def bt(i,curr):
            if i==N:
                ans.append(curr[:])
            else:
                for j in range(i,N):
                    if isPalindrome(i,j):
                        curr.append(s[i:j+1])
                        bt(j+1,curr)
                        curr.pop()
                
        bt(0,[])
        
        return ans
```