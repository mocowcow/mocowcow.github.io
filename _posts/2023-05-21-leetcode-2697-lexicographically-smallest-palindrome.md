--- 
layout      : single
title       : LeetCode 2697. Lexicographically Smallest Palindrome
tags        : LeetCode Easy String TwoPointers Greedy
---
周賽346。

# 題目
輸入由小寫字母組成的字串s，每次動作，你可以將其中一個字母換成另一個字母。  

你的目標是用最少的動作次數使s成為**回文字串**。如果有多種回文都符合最小動作次數，則選擇**字典順序最小**者。  

回傳生成的回文字串。  

# 解法
回文是成對的，也就是說第i個字元和第N-1-i個必須相同。  
若不相同，為了使字典順序最小，則必須將較大的字元改成較小的一方。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        a=list(s)
        l=0
        r=len(s)-1
        
        while l<r:
            if a[l]<a[r]:
                a[r]=a[l]
            elif a[l]>a[r]:
                a[l]=a[r]
            l+=1
            r-=1
        
        return "".join(a)
```
