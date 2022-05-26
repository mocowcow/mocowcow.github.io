---
layout      : single
title       : LeetCode 191. Number of 1 Bits
tags 		: LeetCode Easy BitManipulation
---
Study Plan - Programming Skills Day 2 Operator。  
剛好跟今天的每日題呼應，真巧。

# 題目
輸入一個整數，求以二進位表示有多少個位元1。

# 解法
維護變數cnt，當n>0時將cnt加上n&1，並將n/2。最後cnt就是答案。

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += n & 1
            n >>= 1

        return cnt

```

2022-05-26更新，又是每日題。  
這次比較懶，直接用python內建函數轉成字串，再判斷有多少個1。  

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
```

仔細想想不對，這麼單純的題目應該不會多次出現在每日題。  
逛逛討論區才知道有個特殊的運算：n&(n-)。  
這個運算每次可以把最末端的1改成0，重複這個動作，直到n=0為止。

例如：  
> n = 101, (n-1) = 110  
> n&(n-1) = 100  

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt=0
        while n:
            n&=(n-1)
            cnt+=1
            
        return cnt
```