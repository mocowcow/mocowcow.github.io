--- 
layout      : single
title       : LeetCode 215. Kth Largest Element in an Array
tags        : LeetCode Medium Array Sorting Heap DevideAndconquer 
---
每日題。有挺多種解法，最值得注意的是quick select。  

# 題目
輸入數列nums和整數k，找到nums中第k大的數字。  

# 解法
最簡單暴力也最容易想到的方法，莫過於排序。  
遞減排序後，回傳第k-1個元素。  
複雜度O(N log N)。

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]
```

或是使用min heap，只維護最大的k個元素，而heap最前方的的那個就是第k大的元素。  
複雜度降低至O(N log k)。

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h=[]
        for n in nums:
            heappush(h,n)
            if len(h)>k:
                heappop(h)
                
        return h[0]
```

再來是和quick sort差不多概念的quick select，選擇任意元素x，把nums分成三個區塊：  
左區塊L存比x小的元素；中間區塊M存放等於x的元素；右區塊R存比x大的元素。  

若R大小滿足k，則可以確定答案一定在右區塊中，往右區塊遞迴找第k大的元素。  
若R和L的大小加起來不足k，則確定答案一定在左區塊中，則往左區塊遞迴。但因為R和L中的元素都不是需要的答案，所以要將k扣除這兩塊的大小。  
剩下情況代表答案只可能在中間區塊，而中間區塊只保存x，故回傳x。  

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        x=random.choice(nums)
        L=[]
        M=[]
        R=[]
        for n in nums:
            if n==x:
                M.append(n)
            elif n<x:
                L.append(n)
            else:
                R.append(n)
                
        if len(R)>=k:
            return self.findKthLargest(R,k)
        elif len(R)+len(M)<k:
            return self.findKthLargest(L,k-len(R)-len(M))
        else:
            return x
                                      
```