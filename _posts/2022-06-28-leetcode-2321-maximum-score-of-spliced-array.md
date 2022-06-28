--- 
layout      : single
title       : LeetCode 2321. Maximum Score Of Spliced Array
tags        : LeetCode Hard Array DP Greedy
---
周賽299。看到Q3又是HARD差點嚇死，好在只是虛張聲勢，實際上難度不高。

# 題目
輸入兩個長度為n的子陣列nums1和nums2。  
你可選擇兩個整數left和right，且0 <= left <= right < n，並將兩個子陣列nums1[left...right]和nums2[left...right]互換。
例如：  
> nums1 = [1,2,3,4,5], nums2 = [11,12,13,14,15]  
> left = 1,  right = 2  互換
> nums1 = [1,**12,13**,4,5],  nums2 = [11,**2,3**,14,15].

你可以選擇互換**一次**，或是不互換。  
這兩個陣列的**分數**定義為sum(nums1)和sum(nums2)的最大值，求最大的可能分數為多少。  

# 解法
子陣列互換有兩個重點要考慮：  
1. 要讓nums1還是nums2總和增加  
2. 哪個子陣列的增加值最大  

但沒辦法判斷使哪個陣列增大比較合適，那就兩個都嘗試。  
將目標值扣掉來源值，可以得出每個位置交換後的數值變化量，問題就簡化成kadane maximum subarray。  

寫一個函數f(a1,a2)，代表將a1經過交換後的最大總和。  
維護變數best紀錄最大子陣列，curr代表當前子陣列。遍歷每個索引所對應的兩數字，以交換後的變化量更新curr，再以curr更新最大子ˇ陣列。若curr出現負數則代表當前索引不可能生成總和大於0子陣列，將其捨棄掉。  
最後回傳原本a1的總和加上最大子陣列的值。  

把兩個陣列都丟入f中計算，回傳較大者就是答案。  

```python
class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        
        def f(a1,a2):
            best=curr=0
            for a,b in zip(a1,a2):
                curr=max(0,curr+b-a)
                best=max(best,curr)
                
            return sum(a1)+best
        
        return max(f(nums1,nums2),f(nums2,nums1))
```
