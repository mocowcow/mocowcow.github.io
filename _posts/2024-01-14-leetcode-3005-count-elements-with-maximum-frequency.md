---
layout      : single
title       : LeetCode 3005. Count Elements With Maximum Frequency
tags        : LeetCode Easy Array
---
周賽380。

## 題目

輸入正整數陣列 nums。  

求 nums 中有多少個元素，其出現頻率等於**最大**的元素**出現頻率**。  

## 解法

要看清楚，是問有**幾個**元素的頻率等於最大頻率，不是有**幾種**。  

先遍歷 nums 統計元素頻率。  
在遍歷頻率遍歷找到最大頻率 mx。  
最後遍歷 nums 看有有哪些元素的頻率等於 mx。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = Counter(nums)
        mx = max(d.values())
        
        return sum(d[x] == mx for x in nums)
        # return sum(v for v in d.values() if v == mx)
```

其實只需要一次遍歷。  

舉個例子：  
> nums = [1,1,1,2,2,2,3,3,3]  
> freq = {1:3, 2:3, 3:3}, mx = 3  

可以發現若元素 x 滿足 freq[x] = mx，則 x 會出現 mx 次(好像廢話)，因此可以直接給答案貢獻 mx 個。  
在遍歷 nums 統計頻率途中，一邊維護最大頻率 mx。  
若某個元素的頻率超過 mx，則把答案重置成 mx；又或是碰到其他頻率 mx 的元素，也會對答案貢獻 mx。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ans = 0
        mx = 0
        d = Counter()
        for x in nums:
            d[x] += 1
            
            if d[x] > mx:
                mx = d[x]
                ans = 0
            
            if d[x] == mx:
                ans += d[x]
                
        return ans
```
