--- 
layout      : single
title       : LeetCode 2712. Minimum Cost to Make All Characters Equal
tags        : LeetCode Medium String Array Greedy PrefixSum
---
周賽347。

# 題目
輸入長度n的二進位字串s。你可以執行以下兩種操作任意次：  
- 選擇索引i，將索引0\~i的所有位元反轉，成本為i+1  
- 選擇索引i，將索引i\~n-1的所有位元反轉，成本為n-i  

求將所有位元變成相同的最小成本。  

# 解法
要翻成全部相同只有兩種可能：全0或全1。兩個都嘗試，看哪種成本小。  

翻轉**前x個**等價於翻轉**後N-x個**。如果要翻的位置比較靠左就翻左半邊，靠右就翻右半邊，在正中間隨便都可以。  
而想翻轉左半第x個數，會影響到其他x-1個數，所以要從中心往外翻；右半邊也同理。  

維護變數flip代表翻轉次數，1代表翻過，要將當前的數字翻一次；0則代表不用翻。  
函數f(t)代表嘗試將整個陣列變成t的最小成本，對左右兩半分別從中心往外翻轉，並記錄翻轉成本。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def minimumCost(self, s: str) -> int:
        N=len(s)
        a=[int(c) for c in s]
        
        def f(t):
            cnt=0
            # left part
            flip=0
            for i in reversed(range(N//2)):
                if flip^a[i]!=t:
                    flip^=1
                    cnt+=i+1
            
            # right part
            flip=0
            for i in range(N//2,N):
                if flip^a[i]!=t:
                    flip^=1
                    cnt+=N-i
            return cnt
        
        return min(f(1),f(0))
```
