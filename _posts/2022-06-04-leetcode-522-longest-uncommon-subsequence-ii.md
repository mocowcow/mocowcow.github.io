--- 
layout      : single
title       : LeetCode 522. Longest Uncommon Subsequence II
tags        : LeetCode Medium Array TwoPointers
---
隨便抽的，這題目描述有點奇怪，看了好幾次才懂。

# 題目
輸入字串陣列strs，試著找到之間的最長**非公共子序列**長度。  
**非公共子序列**指的是某個子序列sub是s的子序列，但不是另外所有字串的子序列。  

# 解法
換個簡單易懂的說法，其實就是某個子序列sub只能是其中一個字串的子序列。  

而每個字串s能產生的最長子序列即是自己本身，所以我們只要對遍歷所有strs中所有字串s1，看s1是多少字串的子序列，若剛好為1則代表此為非公共子序列，則以s1的長度更新答案。

判斷子序列的部分使用雙指針，若要找t是否為s的子序列，則以i,j指針分別代表兩字串的處理字元，若成功在s中找到t的所有字元，則回傳true。

```python
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        
        def isSub(s,t):
            i=j=0
            while i<len(s) and j<len(t):
                if s[i]==t[j]:
                    j+=1
                i+=1
            return j==len(t)
        
        ans=-1
        for s1 in strs:
            cnt=0
            for s2 in strs:
                if isSub(s2,s1):
                    cnt+=1
            if cnt==1:
                ans=max(ans,len(s1))
                
        return ans
```
