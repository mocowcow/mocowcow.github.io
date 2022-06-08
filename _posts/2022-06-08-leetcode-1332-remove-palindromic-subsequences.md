--- 
layout      : single
title       : LeetCode 1332. Remove Palindromic Subsequences
tags        : LeetCode Easy String TwoPointers
---
每日題。這題有點誇張，根本超級腦筋急轉彎。查了下發現當次周賽卡死一堆人，怪不得一堆人按爛。  

# 題目
輸入只包含字母'a'和'b'的字串s。你每次可以刪除s的一個回文子序列。  
求使s成為空字串的最小刪除次數。  

# 解法
最佳的狀況是s本身就是回文字串，那麼只需要一步就可以使s為空。  

那麼其他情況怎麼辦？若某個子序列全部為'a'或是'b'，他一定是回文。因為要求最小步數，那麼就一次刪除所有的相同字母。  
所以s本身不為回文的話，則需要兩次刪除。

```python
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return 2
            l+=1
            r-=1
            
        return 1
```

透過字串反轉來檢查回文的一行版本。

```python
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 2-(s==s[::-1])
```