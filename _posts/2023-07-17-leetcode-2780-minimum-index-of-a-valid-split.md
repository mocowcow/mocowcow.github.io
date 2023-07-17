--- 
layout      : single
title       : LeetCode 2780. Minimum Index of a Valid Split
tags        : LeetCode Medium Array HashTable
---
周賽354。

# 題目
對於長度為m的整數陣列arr來說，如果元素x滿足freq(x)\*2 > m，則稱x是**支配元素**。其中freq(x)指的是x在arr中的出現次數，且保證arr**最多一個**支配元素。  

輸入長度n，且有一個支配元素的的整數陣列nums。  

你可以選擇一個索引i，將nums切成兩個陣列，一半是nums[0, ..., i]，另一半是nums[i+1, ... , n-1]。一個**有效**的分割必須滿足：  
- 0 <= i < n - 1  
- 分割出的兩個陣列必須擁有相同的支配元素  

求最小的**有效分割**索引。若不存在答案，則回傳-1。  

# 解法
題目限制分割點讓左右兩個子陣列最少都有一個元素，不必考慮空陣列的特殊情況。  

雖然沒有嚴謹的去證明，但是分割出兩個**支配元素**相同的子陣列，那一定要和原本的**支配元素**dom相同。  
那麼只要枚舉所有索引i作為分割點，只要兩邊的dom分別都超過子陣列長度一半，就代表分割有效，回傳i。  
最後找不到答案，回傳-1。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        N=len(nums)
        dom=None
        dom_cnt=0
        for k,v in Counter(nums).items():
            if v>dom_cnt:
                dom_cnt=v
                dom=k
            
        left_cnt=0
        for i in range(N-1):
            if nums[i]==dom:
                left_cnt+=1
                
            right_cnt=dom_cnt-left_cnt
            lsize=i+1
            rsize=N-lsize
            if left_cnt*2>lsize and right_cnt*2>rsize:
                return i
            
        return -1
```
