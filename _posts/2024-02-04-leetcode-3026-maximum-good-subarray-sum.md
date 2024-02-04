---
layout      : single
title       : LeetCode 3026. Maximum Good Subarray Sum
tags        : LeetCode Medium Array PrefixSum HashTable
---
雙周賽123。

## 題目

輸入長度 n 的整數陣列 nums，還有一個正整數 k。  

若 nums 的一個子陣列，其**第一**和**最後**一個元素的**絕對差**正好為 k，則稱為**好的**。  
也就是說，好的子陣列 nums[i..j] 滿足 |nums[i] - nums[j]| == k。  

求所有好的子陣列之中的**最大**子陣列和。若不存在好的子陣列，則回傳 0。  

## 解法

若某個子陣列的最後一個元素為 nums[j] = x，則第一個元素只能是 **x - k 或 x + k**。  
可以枚舉 x 作為子陣列的最後一個元素，並試著在左方找合法的左邊界。  

對於同一個 j 來說，如果有好幾個合法的候選索引 i，要選擇哪個才能把 nums[i..j] 的和最大化？  
既然要求子陣列區間總和，肯定會想到**前綴和**。  

以前綴和的角度來看，nums[i..j] 相當於 nums[0..j] - nums[0..(i-1)]。  
為了使 nums[i..j] 最大化，必須找到**最小的** nums[0..(i-1)]。  
因此在枚舉的過程中，順便計算前綴和，並以當前 nums[j] = x 為鍵值，維護最小的前綴和。  

注意：子陣列和有可能是負數，因此答案的初始值必須設為**無限小**，否則會更新失敗。  
並且回傳答案前還要特別判定，若答案保持初始值，則回傳 0。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = -inf
        d = defaultdict(lambda: inf)
        ps = 0

        for x in nums:
            d[x] = min(d[x], ps)
            ps += x
            
            ans = max(
                ans,
                ps - d[x + k],
                ps - d[x - k]
            )
        
        if ans == -inf:
            return 0
        
        return ans
```

附上不使用 defaultdict 的版本。  

其實 defaultdict 就只是一個給定預設值的字典，如果以不存在的 key 取值的話就會拿到預設值，而不會報錯。  
用普通字典的話就要一直檢查 key 是否存在。  

```python
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = -inf
        d = {}
        ps = 0

        for x in nums:
            if x not in d or ps < d[x]:
                d[x] = ps
            ps += x
            
            for y in [x + k, x - k]:
                if y in d:
                    ans = max(ans, ps - d[y])
        
        if ans == -inf:
            return 0
        
        return ans
```
