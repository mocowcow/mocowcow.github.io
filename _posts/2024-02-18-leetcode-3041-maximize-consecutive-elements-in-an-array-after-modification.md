---
layout      : single
title       : LeetCode 3041. Maximize Consecutive Elements in an Array After Modification
tags        : LeetCode Hard Array HashTable DP BinarySearch
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

時間複雜度 O(N log N)，瓶頸在於排序。  
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

其實要用熟悉的**填表法**也可以做，但是真的要寫一長串。  

一樣排序後，試著求出以 nums[i] 結尾的最大長度。  
只不過 nums[i] 可以選擇是否加 1，所以需要額外的變數 inc_i 來表示此狀態。  

所以實際結尾的元素是 target = nums[i] + inc_i。  
我們要在 nums[0..i-1] 之間找到等於 target - 1 元素 nums[j]，並把 target 接在後面。  
同樣的，nums[j] 也可以增加值，所以對於 nums[j] 和 nums[j] + 1 兩種結尾的子序列都要找。  

---

但相同的 nums[j] 可能存在好幾個，總不可能每個都遍歷。而實際上只要取最後一個就行。  
因為陣列是有序的，相同的元素越靠右邊，越有可能使得子序列變長。  
實際上相同元素 x 出現第三次之後都沒有用。試想以下例子：  
> nums = [1,2,2]  
> nums[0] = 1 結尾 = [1]  
> nums[0] + 1 = 2 結尾 = [2]  
> nums[1] + = 2 結尾 = [1,2]  
> nums[1] + 1 = 3 結尾 = [1,2]  
> nums[2] + = 2 結尾 = [1,2]  
> nums[2] + 1 = 3 結尾 = [1,2,3]  

相同的元素 x 出現第二次，頂多當作 x+1 來用，把上次 x 結尾的子序列變長一格。  
之後在出現根本沒意義。  
在有序的陣列中找到特定值，很明顯就是靠**二分搜**了。  

---

定義dp(i, inc_i)：以 nums[i] + inc_i 結尾的最長子序列。  
轉移：dp(i, inc_i) = max( dp(j, inc_j) + 1 ) FOR ALL 0 <= j < i AND nums[j] + inc_j + 1 = nums[i] + inc_i
邊界：當 i = 0 時，子序列只有自己一個元素，回傳 1。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        
        @cache
        def dp(i, inc_i):
            if i == 0:
                return 1
            res = 1
            target = nums[i] + inc_i
            for inc_j in range(2):
                # find last nums[j] + inc_j + 1 < target
                lo = 0
                hi = i - 1
                while lo < hi:
                    mid = (lo + hi + 1) // 2
                    if nums[mid] + inc_j >= target:
                        hi = mid - 1
                    else:
                        lo = mid
                j = lo
                if nums[j] + inc_j + 1 ==  target:
                    res = max(res, dp(j, inc_j) + 1)
            return res
        
        ans = 0
        for i in range(N):
            for inc_i in range(2):
                ans = max(ans, dp(i, inc_i))
        
        return ans
```
