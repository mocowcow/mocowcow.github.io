---
layout      : single
title       : LeetCode 2974. Minimum Number Game
tags        : LeetCode Easy Array Sorting Simulation
---
周賽377。

## 題目

輸入**偶數長度**的整數陣列nums。最初還有一個空陣列arr。  

Alice和Bob在玩遊戲，每回合，Alice和Bob都會各執行一次動作。  
規則如下：  

- 每回合，Alice先移除nums中的最小元素。然後Bob也移除一個最小元素  
- 然後Bob將他剛移除的元素加到arr中。然後Alice也將他移除的元素加到arr中  

回傳最終arr的結果。  

## 解法

按照題意模擬即可。  

時間複雜度O(N log N)。  
空間複雜度O(1)，答案空間不計。  

```python
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        ans=[]
        for i in range(0,len(nums),2):
            ans.append(nums[i+1])
            ans.append(nums[i])
            # or smiply swap the pairs
            # nums[i],nums[i+1]=nums[i+1],nums[i]
            
        return ans
```
