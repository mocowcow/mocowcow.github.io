---
layout      : single
title       : LeetCode 3041. Maximize Consecutive Elements in an Array After Modification
tags        : LeetCode Hard Array HashTable DP
---
雙周賽124。根本沒想到又是 dp，想著二分罰坐一小時。  

## 題目

輸入正整數陣列 nums。  

最初，你可以選擇陣列中**任意**個元素，並將其值加 1。  

修改後，你必須選擇一或多個元素，這些元素排序後，是滿足**相鄰遞增**的。  
例如 [3, 4, 5] 滿足，但 [3, 4, 6] 和 [1, 1, 2, 3] 不滿足。  

求**最多**可以選擇幾個元素。  

## 解法

在陣列中選擇任意元素後排列，相當於選擇**子序列**。  
子序列順序不影響答案，而且檢查**相鄰遞增**也要維持有序。總之先把 nums 排序。  

對於 nums 中的每個元素 x，有兩種使用方案：  

- 加 1，把 x+1 連接在 x 結尾的子序列上  
- 保持不變，把 x 連接在 x-1 結尾的子序列上  

---

我們在乎的是以**某元素 x 結尾**的最大長度，因此是以**值域**作為 dp 的狀態，而非普遍的使用的元素**索引**。  
另外還有一個不同點的，大多數 dp 都是從多個來源轉移到一個狀態，稱為**填表法**；這次是用一個值 x 去更新多個狀態，稱為**刷表法**。  

定義 dp(i)：以 i 作為結尾的**最大**子序列長度。  
轉移：dp[i+1] = dp[i]；dp[i] = dp[i-1]  

需要注意的是，對於元素 x，一定要先更新 dp[x+1] 後才更新 dp[x]，否則會得到錯誤的答案。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = Counter()
        
        for x in nums:
            dp[x+1] = dp[x] + 1
            dp[x] = dp[x-1] + 1
            
        return max(dp.values())
```
