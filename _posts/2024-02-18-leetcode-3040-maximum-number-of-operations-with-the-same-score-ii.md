---
layout      : single
title       : LeetCode 3040. Maximum Number of Operations With the Same Score II
tags        : LeetCode Medium Array DP
---
雙周賽124。久違一個多月的 dp，最近幾乎都是考字串。  

## 題目

輸入整數陣列 nums，若 nums 中有至少 2 個元素，則可以重複進行以下操作：  

- 選擇最前面的兩個元素並刪除  
- 選擇最後面的兩個元素並刪除  
- 選擇第一個、和最後一個元素並刪除  

每次操作的**分數**為刪除元素的加總。  

你的目標是求**最多**可以執行幾次操作，且每次分數相同。  

## 解法

第一次操作會決定之後的**分數限制**。最多會有三種不同的分數限制。  
不同的操作順序有可能導致相同的剩餘元素，有**重疊的子問題**，因此考慮 dp。  

定義 dp(i, j, score)：在子陣列為 nums[i..j] 的情況下，能夠執行分數為 score 的最大操作次數。  
轉移：

- dp(i+1, j-1, score) + 1
- dp(i+2, j, score) + 1
- dp(i, j-2, score) + 1  

從操作分數為 score 者取做大值。  

邊界：當 i >= j 時，代表剩餘元素不足 2 個，無法繼續操作，回傳 0。  

---

記得第一次操作有三種選擇，答案就是三者取最大值。  

時間複雜度 O(N^2)。  
空間複雜度 O(N^2)。  

```python
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        N = len(nums)
        
        @cache
        def dp(i, j, score):
            if i >= j:
                return 0
            
            res = 0
            if nums[i] + nums[j] == score:
                res = max(res, dp(i+1, j-1, score) + 1)
                
            if nums[i] + nums[i+1] == score:
                res = max(res, dp(i+2, j, score) + 1)
                
            if nums[j-1] + nums[j] == score:
                res = max(res, dp(i, j-2, score) + 1)
                
            return res
        
        return max(
            dp(0, N-1, nums[0] + nums[-1]),
            dp(0, N-1, nums[0] + nums[1]),
            dp(0, N-1, nums[-1] + nums[-2])
        )
```
