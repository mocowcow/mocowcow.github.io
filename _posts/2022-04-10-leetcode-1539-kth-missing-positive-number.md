---
layout      : single
title       : LeetCode 1539. Kth Missing Positive Number
tags 		: LeetCode Easy Greedy BinarySearch 
---
一樣是學習計畫中的，不過這題就沒什麼人按爛，兩題概念明明差不多，真奇怪。

# 題目
輸入陣列arr以及整數k。從1開始數，求第k個沒arr中出現的數字是多少。

# 解法
一樣暴力貪心，n紀錄當前數字，i紀錄arr中輪到第幾個。如果n不等於arr[i]才把k遞減，重複到k沒有為止。

```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n=0
        i=0
        N=len(arr)
        while k:
            n+=1
            if i<N and arr[i]==n:
                i+=1
            else:
                k-=1
       
        return n
```

改成set更清楚。  

```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s=set(arr)
        n=0
        while k:
            n+=1
            if n not in s:
                k-=1
                
        return n
```

重點的二分搜。  
這公式是難想了一點，說是medium程度也不為過。  
在arr[i]以前且沒在arr中出現的數字有arr[i]-i-1個。
例如： 
> arr = [2,3,4,7,11], k = 5  
> i=0, arr[0]=2, 在2以前有2-0-1個不在arr的數字  
> i=1, arr[3]=3, 在3以前有3-1-1個不在arr的數字  
> ...
> i=4, arr[4]=11, 在11以前有11-4-1個不在arr的數字  

下界為0，是arr中的第一個位置，上界為N，用來搜第mid個位置。如果上界用N-1的話，arr長度剛好為1時就會出錯。  
如果沒出現的數字不足k，更新下界為mid+1，否則更新上界為mid。最後停止時，代表正好有lo個數出現在arr中，所以答案就是lo+k。

```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lo=0
        hi=len(arr)
        while lo<hi:
            mid=(lo+hi)//2
            if arr[mid]-mid-1<k:
                lo=mid+1
            else:
                hi=mid
        
        return lo+k
```