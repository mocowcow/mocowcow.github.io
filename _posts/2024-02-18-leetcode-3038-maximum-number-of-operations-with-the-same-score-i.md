---
layout      : single
title       : LeetCode 3038. Maximum Number of Operations With the Same Score I
tags        : LeetCode Medium Array Simulation
---
雙周賽124。這題很有良心，範例給的是奇數長度，不然肯定死一片。  

## 題目

輸入整數陣列 nums，若 nums 中有至少 2 個元素，則可以重複進行以下操作：  

- 選擇最前面的兩個元素並刪除  

每次操作的**分數**為刪除元素的加總。  

你的目標是求**最多**可以執行幾次操作，且每次分數相同。  

## 解法

題目保證 nums 長度至少 2，那至少可以操作一次。之後每次都要跟第一次分數一樣。  
直接模擬，先求出第一次的分數，然後每次往後跳 2 格。  

在 nums 為奇數長度時，會有一個落單的元素，記得判斷邊界。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        N = len(nums)
        score = nums[0] + nums[1]
        
        ans = 0
        for i in range(0, N, 2):
            if i+1 < N and nums[i] + nums[i+1] == score:
                ans += 1
            else:
                break
                
        return ans
```

對於奇數長度的處理有幾種方式：  

- 基本款，在迴圈內檢查 i+1 是否出界  
- 若是長度 N 為奇數，則把 N 減 1，調整成偶數  
- 直接把 N 除 2 下取整，再乘 2，一定是偶數  

雖然以上方式都可以，但總覺得有點醜。  
看了幾個人的寫法，最優雅的方案是：  

> 直接把 N 減 1  

直接看例子：  
> N = 4  
> 枚舉 [0, N-1) = [0, 3) 的偶數  
> i = [0, 2]  
> N = 5
> 枚舉 [0, N-1) = [0, 4) 的偶數
> i = [0, 2]  

效果剛好相同。  
