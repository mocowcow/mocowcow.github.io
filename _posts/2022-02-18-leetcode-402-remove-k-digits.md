---
layout      : single
title       : LeetCode 402. Remove K Digits
tags 		: LeetCode Medium MonotonicStack Stack
---
每日題。格式處理還是挺麻煩的，善用內建函數快樂許多。

# 題目
輸入長度N的字串num、整數k，求num移除k個數字後可以得到的最小結果。  
k一定小於等於N。

# 解法
想要得到最小的結果，越靠左的位數當然是越小越好。  
維護單調遞增堆疊st，存放可使用的位數。
遍歷num中所有位數n，在k還有剩餘時，若n小於上一位數，則移除該位數。最後再將n押入堆疊。 

一開始沒考慮到特殊情形，例如num='111', k=3，答案應為'0'，但卻輸出'111'。所以要在下方處理該狀況。當遍歷完num時，若k還有剩餘，則將堆疊pop出k次(因為是遞增，後方數字一定較大)。  

最後處理堆疊，題目要求左方不可以有多餘的0，把不要的0全部處理掉。  
但像是num='100', k=1時，答案應為'0'，但st=['0','0']，把0弄掉的話堆疊會為空。當堆疊為空時直接回傳'0'，否則回傳串接好的st。

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for n in num:
            while k and st and n < st[-1]:
                k -= 1
                st.pop()
            st.append(n)

        while k:
            st.pop()
            k -= 1

        ans = ''.join(st).lstrip('0')
        return ans if ans else '0'

```

看看別人的解法，發現or運算子的神奇妙用：return A or B，如果A是falsy的話就會回傳B。
經過改良的程式碼如下。

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if num == '0' or len(num) == k:
            return '0'
            
        st = []
        for n in num:
            while k and st and st[-1] > n:
                k -= 1
                st.pop()
            st.append(n)

        if k:
            st = st[:-k]

        return ''.join(st).lstrip('0') or '0'
```