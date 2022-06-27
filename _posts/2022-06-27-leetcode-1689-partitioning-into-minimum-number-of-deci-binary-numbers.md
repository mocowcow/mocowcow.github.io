--- 
layout      : single
title       : LeetCode 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
tags        : LeetCode String Greedy
---
每日題。八點起床寫扣的感覺真好。題目的deci-binary還真難想到對應的中文翻譯，就算只看英文其實也是滿模糊的。  

# 題目
如果一個十進位數字沒有前導零，且只有出現數字0和1，那該數字稱為**十又二進位數字**，例如101和110；而112和3001則不是。  
輸入字串n，代表一個十進位正整數，求最少需要多少個**十又二進位數字**才能使總和達到n。  

# 解法
其實只看描述還真不太確定題目想表達什麼，好在有例題1有詳細解釋：  
> 32 = 10 + 11 + 11  

反正就是把一個整數拆成好幾個只包含1和0的整數，且越少越好。  
但每一個整數最多只能對某個位數增加1，所以需要的數量取決於所有位數中的最大值。  

```python
class Solution:
    def minPartitions(self, n: str) -> int:
        ans=1
        for c in n:
            ans=max(ans,int(c))
            
        return ans
```

仔細想想，答案只取決於每個位數中的最大值，那麼可以從9開始往下找，若某個值有出現過，則直接回傳。  
執行起來有夠快，才42ms，勝過99.24%的提交。

```python
class Solution:
    def minPartitions(self, n: str) -> int:
        for c in '987654321':
            if c in n:return c
```

最後是搞笑python解法。  
字串本身是iterable，丟給max函數會把字串拆成好幾個字元，並回傳其中最大者。  
leetcode本身不管回傳值型別，只要答案轉回字串後相同就算正確。  

```python
class Solution:
    def minPartitions(self, n: str) -> int:
        return max(n)
```
