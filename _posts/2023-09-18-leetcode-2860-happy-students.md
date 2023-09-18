---
layout      : single
title       : LeetCode 2860. Happy Students
tags        : LeetCode Medium Array Sorting Greedy
---
周賽363。描述有點怪，我不知道學生究竟開不開心，反正我是不太開心。  

## 題目

輸入長度n的整數陣列nums，代表班級有n個學生。  
老師想要選擇一群學生，並且讓他們全都開心。  

如果滿足以下條件，則第i個學生會開心：  

- 該學生**有被選擇**，且被選總人數**嚴格大於**nums[i]  
- 該學生**沒被選擇**，且被選總人數**嚴格小於**nums[i]  

求有多少選擇方式使得全部學生都開心。  

## 解法

反正不在乎學生的順序，就先排序吧。  

設選擇人數為choose，若要開心，則**有選的**都要小於choose；**沒選的**都要大於choose。  
為了盡可能滿足這條件，那麼應當優先選擇較小的nums[i]。  

如果選了nums[i]，那麼所有小於等於nums[i]的學生都要選，才能滿足**有選的都小於choose**。  
那麼我們遍歷排序好的nums，枚舉選前i+1個學生的情形，這時**有選的**學生最大值就是nums[i]，要確保nums[i]小於choose；從nums[i+1]開始都是沒選的，要確保nums[i+1]大於choose。  
同時滿足兩者就答案加1。  

範例很好心，告訴我們**選0個**也是一種方案。  
如果nums[0]大於0，答案要再加1。  

選N個學生，就沒有nums[i+1]會出界，不要忘記檢查邊界。  

時間複雜度O(n log n)。  
空間複雜度O(1)。  

```python
class Solution:
    def countWays(self, nums: List[int]) -> int:
        N=len(nums)
        nums.sort()
        ans=0
        
        if nums[0]>0:
            ans=1
            
        for i,x in enumerate(nums):
            choose=i+1
            if x<choose and (i+1==N or nums[i+1]>choose):
                ans+=1
            
        return ans
```

在仔細看看，發現所有nums[i]都小於N，所以選了全部N個學生的情況下，所有學生都小於choose的，直接加1。  

```python
class Solution:
    def countWays(self, nums: List[int]) -> int:
        N=len(nums)
        nums.sort()
        ans=0
        
        if nums[0]>0:
            ans=1
            
        for i in range(N-1):
            choose=i+1
            if nums[i]<choose and nums[i+1]>choose:
                ans+=1
            
        return ans+1
```
