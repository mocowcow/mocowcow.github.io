--- 
layout      : single
title       : LeetCode 2574. Left and Right Sum Differences
tags        : LeetCode Easy Array PrefixSum
---
周賽334。

# 題目
輸入整數陣列nums，並找到陣列answer，符合：  
- answer.length == nums.length  
- answer[i] = |leftSum[i] - rightSum[i]|  

其中：  
- leftSum[i]是索引i左方所有元素的總和。若無元素則為0  
- rightSum[i]是索引i右方所有元素的總和。若無元素則為0  

回傳陣列answer。  

# 解法
初始化right為nums總和，left為0。  
從最左開始遍歷nums中的數字n，將right扣掉n後得到right正確值。更新答案後再把n加到left去。  

時間複雜度O(N)。空間複雜度O(1)。  

```python
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        right=sum(nums)
        left=0
        ans=[]
        
        for n in nums:
            right-=n
            ans.append(abs(right-left))
            left+=n
            
        return ans
```
