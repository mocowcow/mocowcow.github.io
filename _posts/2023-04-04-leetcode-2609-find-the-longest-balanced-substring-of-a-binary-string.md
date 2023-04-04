--- 
layout      : single
title       : LeetCode 2609. Find the Longest Balanced Substring of a Binary String
tags        : LeetCode Easy String
---
周賽339。需求簡單明瞭，但就是不太好實踐，不小心又WA一次。  

# 題目
輸入只由0和1組成的二進位字串s。  

若s的一個子字串中，全部的0都在1的左方，且0和1出現次數相等，則稱為**平衡的**。注意，空字串也是平衡的。  

求s的**最長**平衡子字串。  

# 解法
首先要找一串連續的0，然後再找一串連續的1，最後取兩個成對的次數，乘上2就是平衡子字串長度。  

分類討論一下：　　
- 當前為0，如果前一個是1，就要全部清空；否則繼續累加  
- 當前為1，直接把1的計數累加，然後取0和1的最小值更新答案  

最後回傳最大成對數量ans*2就是答案。  

時間複雜度O(N)。空間複雜度O(1)。  

```python
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        zero=0
        one=0
        ans=0
        prev=None
    
        for c in s:
            if c=="0":
                if prev=="1":
                    zero=one=0
                zero+=1
            else:
                one+=1
                ans=max(ans,min(zero,one))
                
            prev=c
                
        return ans*2
```

其實最方便的解法應該是內建字串查找。  

從空字串""開始，如果存在於s之中，則外層多包一次0和1，繼續查找。直到找不到為止，答案應該是上一次的查找結果。  

在s中找t的複雜度為O(len(s) + len(t))，最多查找N/2次，t長度最大為N，時間複雜度O(N^2)。空間複雜度O(N)。  

```python
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        pat=""
        
        while pat in s:
            pat="0"+pat+"1"
            
        return len(pat)-2
```