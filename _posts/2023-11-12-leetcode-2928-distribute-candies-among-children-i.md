---
layout      : single
title       : LeetCode 2928. Distribute Candies Among Children I
tags        : LeetCode Easy Simulation Math
---
雙周賽117。最近周賽真的是越來越扯，前兩題分別是分糖果1和2。但是在開賽的前幾日，分糖果3竟然以**付費題**的形式出現。  
而且內容完全一樣，只是測資範圍變大，直接向下兼容本次兩題。真的是pay to win。  

## 題目

輸入兩個正整數n和limit。  

把n個糖果分給3個小孩，且每個小孩最多拿limit個糖果。求有多少分法。  

## 解法

首先是暴力法，枚舉三個小孩的糖果數，剛好對上總數n就合法。  

時間複雜度O(limit^3)。  
空間複雜度O(1)。  

```python
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans=0
        for i in range(limit+1):
            for j in range(limit+1):
                for k in range(limit+1):
                    if i+j+k==n:
                        ans+=1
                        
        return ans
```

如果只枚舉第一個小孩i，剩下j+k兩個小孩的糖果數會是n-i=jk。  
分類討論三種情況：  

1. jk不超過limit。則j小孩可以隨便拿，然後k撿剩的  
2. jk超過limit，不超過兩倍limit，當j在某個區間時，正好可以分完  
3. jk超過兩倍limit。兩人無法分完  

情況1，j可以隨便拿[0, jk]個，剩下給k一定合法。  
情況3不處理。  
至於情況2，我們要找出j在哪個區間才會合法。  

j最多肯定可以拿到limit個，故上界是limit。  
如果j拿越少，則k拿的會越多。當j少到一個臨界值min(j)，會使得k超過limit。  
必須滿足jk-j <= limit。  

> 以min(j)帶入j  
> jk-min(j) <= limit  
> 移項  
> jk-limit <= min(j)  

得到min(j) = jk-limit，這就是下界。  
所以j的範圍是[min(j), limit]。  

時間複雜度O(limit)。  
空間複雜度O(1)。  

```python
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        limit=min(limit,n)
        ans=0
        for i in range(limit+1):
            jk=n-i
            if jk<=limit:
                ans+=jk+1
            elif jk<=limit*2:
                hi=limit
                lo=jk-limit
                ans+=hi-lo+1
                
        return ans
```
